# Generated by Django 3.0.3 on 2020-04-18 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_article_article_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='html',
            field=models.CharField(default='', max_length=200),
        ),
    ]
