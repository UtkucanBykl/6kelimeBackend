# Generated by Django 2.1.5 on 2019-02-23 20:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('OPEN', 'Open'), ('CLOSE', 'Close'), ('INSPECTING', 'Inspecting')], default='OPEN', max_length=10)),
                ('name', models.CharField(max_length=140, verbose_name='Ad')),
            ],
            options={
                'verbose_name': 'Kategori',
                'verbose_name_plural': 'Kategoriler',
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('OPEN', 'Open'), ('CLOSE', 'Close'), ('INSPECTING', 'Inspecting')], default='OPEN', max_length=10)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL, verbose_name='Takip Eden')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL, verbose_name='Takip Edilen')),
            ],
            options={
                'verbose_name': 'Takip',
                'verbose_name_plural': 'Takipler',
            },
        ),
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='core.Post', verbose_name='Gönderi'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=140, verbose_name='İçerik'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.BooleanField(default=True, verbose_name='Görünür mü?'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı'),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('user', 'post')},
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='core.Category', verbose_name='Kategori'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('follower', 'following')},
        ),
    ]
