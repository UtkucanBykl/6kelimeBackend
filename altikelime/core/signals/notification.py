from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from ..models import Like, Comment, Follow, Notification


__all__ = ['create_like_notification',
           'create_comment_notification',
           'create_follow_notification',
           'delete_comment_notification',
           'delete_like_notification',
           'delete_follow_notification']


@receiver(post_save, sender=Like)
def create_like_notification(sender, instance=None, created=False, **kwargs):
    if created:
        message = f'{instance.user.username} adlı kullanıcı gönderini beğendi'
        Notification.objects.create(
            receiver=instance.post.user,
            message=message,
            notification_type='LIKE',
            post=instance.post,
            sender=instance.user
        )

@receiver(post_delete, sender=Like)
def delete_like_notification(sender, **kwargs):
    notification_qs = Notification.objects.filter(
        post=kwargs['instance'].post,
        receiver=kwargs['instance'].post.user,
        sender=kwargs['instance'].user,
        notification_type='LIKE'
    )
    if notification_qs.exists():
        notification_qs.delete()

@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance=None, created=False, **kwargs):
    if created:
        message = f'{instance.user.username} adlı kullanıcı gönderine yorum attı'
        Notification.objects.create(
            receiver=instance.post.user,
            message=message,
            notification_type='COMMENT',
            post=instance.post,
            sender=instance.user
        )

@receiver(post_delete, sender=Comment)
def delete_comment_notification(sender, **kwargs):
    notification_qs = Notification.objects.filter(
        post=kwargs['instance'].post,
        receiver=kwargs['instance'].post.user,
        sender=kwargs['instance'].user,
        notification_type='COMMENT'
    )
    if notification_qs.exists():
        notification_qs.delete()

@receiver(post_save, sender=Follow)
def create_follow_notification(sender, instance=None, created=False, **kwargs):
    if created:
        message = f'{instance.follower.username} adlı kullanıcı seni takip etti'
        Notification.objects.create(
            receiver=instance.following,
            message=message,
            notification_type='FOLLOW',
            sender=instance.follower
        )

@receiver(post_delete, sender=Follow)
def delete_follow_notification(sender, **kwargs):
    notification_qs = Notification.objects.filter(
        receiver=kwargs['instance'].following,
        notification_type='FOLLOW',
        sender=kwargs['instance'].follower
    )
    if notification_qs.exists():
        notification_qs.delete()

