from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import (CreateView,
                                  DeleteView,
                                  ListView,
                                  RedirectView,
                                  View
                                  )
from django.contrib.auth.mixins import PermissionRequiredMixin as PRM
from django.contrib.auth.mixins import LoginRequiredMixin as LRM
# from django.contrib import messages
from .models import Post, Report
from .forms import PostForm
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth import get_user_model


class PostFormListView(CreateView):
    form_class = PostForm
    template_name = "posts/post_form.html"
    success_url = reverse_lazy('posts:post-form')

    def get_queryset(self):
        return Post.objects.filter(hidden=False).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.get_queryset()
        return context

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return super().form_valid(form)


class PostDelete(LRM,DeleteView):
    """only user who wrote a post can delete it"""
    model = Post
    success_url = reverse_lazy('posts:post-form')

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)


class ReportListView(LRM,PRM, ListView):
    """in report view not a list of reports but list of posts with attr times_reported
    where total count report saved"""
    permission_required = ['posts.view_report']
    context_object_name = 'reports'
    template_name = 'posts/report_list.html'

    def get_queryset(self):
        return Post.objects.annotate(times_reported=Count('report')).filter(times_reported__gt=0).all()


class ReportPost(LRM,RedirectView):
    http_method_names = ("post",)

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy("posts:post-form")

    def post(self, request, *args, **kwargs):
        """report post avoiding dubble reporting
        method .get_or_create provides the uniqueness of reported_user"""
        post_pk = kwargs.get("pk")
        print("post_id", post_pk)
        post = get_object_or_404(Post, pk=post_pk)

        report, created = Report.objects.get_or_create(
            post=post,
            reported_by=request.user
        )
        report.save()
        return super().post(request, *args, **kwargs)


class PostHide(LRM,PRM, RedirectView):
    permission_required = ('posts.change_post',)

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy("posts:report-list")

    def post(self, request, *args, **kwargs):
        post_to_hide = get_object_or_404(Post, id=self.kwargs.get('pk'))
        if not post_to_hide.hidden:
            post_to_hide.hidden = True
        post_to_hide.date_hidden = timezone.now()
        post_to_hide.deleted_by = request.user
        post_to_hide.save()
        return super().post(request, *args, **kwargs)


class BlockUser(LRM,PRM, RedirectView):
    permission_required = ('users.change_user',)

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy("posts:report-list")

    def post(self, request, *args, **kwargs):
        print("user id from kwargs:", kwargs.get('pk'))
        User = get_user_model()
        user = get_object_or_404(User, id=kwargs.get('pk'))
        print("user to ban", user, user.is_active)

        for post in user.posts.all():
            if not post.hidden:
                post.hidden = True
                post.date_hidden = timezone.now()
                post.deleted_by = request.user
                post.save()
        user.is_active = False
        user.save()
        return super().post(request, *args, **kwargs)
