from django.db import models

from ..models import BaseModel

__all__ = ['Comment']


class Comment(BaseModel):

    user = models.ForeignKey(verbose_name='Kullanıcı', to='auth.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(verbose_name='Gönderiler', to='Post', related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField(verbose_name="Yorum", max_length=200)
    publish = models.BooleanField(verbose_name="Gözükür mü?", default=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Yorum"
        verbose_name_plural = "Yorumlar"
        unique_together = ("user", "post")

    def __str__(self):
        return self.comment
