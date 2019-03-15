from unittest import TestCase

from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from ..models import Like, Comment, Follow, Notification, Post, Category

__all__ = ['NotificationTestCase']


class NotificationTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='hikmet', email='a@a.com')
        self.user.set_password('123456')
        self.user.save()
        self.user2 = User.objects.create(username='utku', email='aa@a.com')
        self.user2.set_password('123456')
        self.user2.save()
        self.category = Category.objects.create(name='Cat1')
        self.post = Post.objects.create(user=self.user, content="1 2 3 4 5 6", category=self.category)

    def test_like_signals(self):
        Like.objects.create(user=self.user2, post=self.post)
        self.assertEqual(
            Notification.objects.filter(receiver=self.post.user, sender=self.user2, post=self.post, notification_type='LIKE').count(),
            1
        )

    def test_comment_signals(self):
        Comment.objects.create(user=self.user2, post=self.post, comment='12313')
        self.assertEqual(
            self.user.notifications.filter(sender=self.user2, post=self.post, notification_type='COMMENT').count(),
            1
        )

    def test_follow_signals(self):
        Follow.objects.create(follower=self.user2, following=self.user)
        self.assertEqual(
            self.user.notifications.filter(sender=self.user2, notification_type='FOLLOW').count(),
            1
        )
