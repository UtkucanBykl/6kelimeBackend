from django.db import models

from ..models import BaseModel

__all__ = ['Notification']


class Notification(BaseModel):
    NOTIFICATION_TYPE = (
        ('FOLLOW', 'Follow'),
        ('LIKE', 'Like'),
        ('COMMENT', 'Comment')
    )
    sender = models.ForeignKey('auth.User', related_name='history', on_delete=models.CASCADE)
    receiver = models.ForeignKey('auth.User', related_name='notifications', on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=32, choices=NOTIFICATION_TYPE, default='LIKE')
    message = models.CharField(max_length=140)
    is_open = models.BooleanField(default=False)
    post = models.ForeignKey('core.Post', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} {self.message}'
