# Generated by Django 3.1.1 on 2020-11-22 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'ordering': ['-note_last_time'], 'verbose_name': '笔记信息', 'verbose_name_plural': '笔记信息'},
        ),
    ]