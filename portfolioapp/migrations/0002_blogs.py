# Generated by Django 5.0.1 on 2024-01-29 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=25)),
                ('img', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
