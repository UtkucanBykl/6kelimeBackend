import random

from django.db import models
from django.utils.text import slugify

from ..models import BaseModel

__all__ = ['Post', 'Like']


class Post(BaseModel):

    user = models.ForeignKey(verbose_name='Kullanıcı', to='auth.User', related_name='posts', on_delete=models.CASCADE)
    content = models.CharField('İçerik', max_length=140)
    publish = models.BooleanField('Görünür mü?', default=True)
    category = models.ForeignKey(verbose_name='Kategori', to='Category', related_name='posts', on_delete=models.CASCADE)
    slug = models.SlugField(editable=False, unique=True)

    class Meta:
        verbose_name = 'Gönderi'
        verbose_name_plural = 'Gönderiler'

    def __str__(self):
        return self.content

    def save(self, **kwargs):
        self.slug = slugify(f'{self.content}-{random.randint(0, 1000)}')
        return super(Post, self).save(**kwargs)


class Like(BaseModel):

    user = models.ForeignKey(verbose_name='Kullanıcı', to='auth.User', related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(verbose_name='Gönderi', to='Post', related_name='likes', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Beğeni'
        verbose_name_plural = 'Beğeniler'
        unique_together = ('user', 'post')

    def __str__(self):
        return f'{self.user.username} liked {self.post.content}'
