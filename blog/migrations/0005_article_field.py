# Generated by Django 3.0.3 on 2020-06-17 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_article_html'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='field',
            field=models.CharField(default='', max_length=20),
        ),
    ]
