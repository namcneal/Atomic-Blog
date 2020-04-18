# Generated by Django 3.0.3 on 2020-04-18 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'publish')], default=0)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('subtitle', models.CharField(max_length=400)),
                ('article_id', models.IntegerField()),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
