from django.db import models

from ..models import BaseModel

__all__ = ['Follow']


class Follow(BaseModel):
    follower = models.ForeignKey(
        verbose_name='Takip Eden',
        to='auth.User',
        related_name='followings',
        on_delete=models.CASCADE
    )
    following = models.ForeignKey(
        verbose_name='Takip Edilen',
        to='auth.User',
        related_name='followers',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('follower', 'following')
        verbose_name = 'Takip'
        verbose_name_plural = 'Takipler'

    def __str__(self):
        return f'{self.follower.username} follow {self.following.username}'
