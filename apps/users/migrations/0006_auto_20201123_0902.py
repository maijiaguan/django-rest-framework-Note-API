# Generated by Django 3.1.1 on 2020-11-23 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20201122_2059'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='code',
            options={'ordering': ['-add_time'], 'verbose_name': '验证码表', 'verbose_name_plural': '验证码表'},
        ),
    ]