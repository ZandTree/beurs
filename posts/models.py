from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=255, default="")
    count = models.SmallIntegerField(default=0)
    hidden = models.BooleanField(default=False)
    date_hidden = models.DateTimeField(null=True, blank=True)
    deleted_by = models.ForeignKey(User,
                                   on_delete=models.DO_NOTHING,
                                   blank=True,
                                   null=True,
                                   related_name="moderator")

    def __str__(self):
        return f'Written by {self.user}'

    class Meta:
        permissions = (('can_mark_inappropriate', 'can mark as inappropr'),)


class Report(models.Model):
    reported_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"done by:{self.reported_by} on post {self.post.id}"
