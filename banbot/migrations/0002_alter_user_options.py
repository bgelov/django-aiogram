# Generated by Django 4.2.3 on 2023-07-20 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banbot', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'администратора', 'verbose_name_plural': 'администраторы'},
        ),
    ]
