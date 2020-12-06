# Generated by Django 3.1.1 on 2020-11-18 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NotesFolder',
            fields=[
                ('folder_uid', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('folder_name', models.CharField(default='未命名', max_length=30, verbose_name='标签名')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_folder', to='category.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_folder', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('note_uid', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note_title', models.CharField(default='未命名', max_length=50, verbose_name='标题')),
                ('note_last_time', models.DateField(verbose_name='最新编辑时间')),
                ('note_content_v1', models.TextField(blank=True, null=True, verbose_name='笔记v1')),
                ('note_content_v2', models.TextField(blank=True, null=True, verbose_name='笔记v2')),
                ('note_content_v3', models.TextField(blank=True, null=True, verbose_name='笔记v3')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_notes', to='category.category')),
                ('folder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='folder_notes', to='noteapp.notesfolder')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_notes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '笔记信息',
                'verbose_name_plural': '笔记信息',
            },
        ),
    ]