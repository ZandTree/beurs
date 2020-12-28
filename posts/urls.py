from django.urls import path
from .views import (PostFormListView,
                    PostDelete,
                    PostHide,
                    ReportListView,
                    ReportPost,
                    BlockUser,
                    )

app_name = 'posts'

urlpatterns = [
    path('',PostFormListView.as_view(),name="post-form"),
    path('delete-post/<int:pk>/',PostDelete.as_view(),name="post-delete"),
    path('hide-post/<int:pk>/',PostHide.as_view(),name="post-hide"),
    path('reports/',ReportListView.as_view(),name="report-list"),
    path('report-post/<int:pk>/',ReportPost.as_view(),name="report-post"),
    path('block-user/<int:pk>/',BlockUser.as_view(),name="ban-user"),
]