# Generated by Django 2.0.7 on 2018-08-18 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_article_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
    ]
