# Generated by Django 3.1.2 on 2020-10-14 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20201014_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_published',
            field=models.BooleanField(default=False, verbose_name='Published'),
        ),
    ]
