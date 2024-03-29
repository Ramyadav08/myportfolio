# Generated by Django 5.0.1 on 2024-01-30 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0004_remove_blogs_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='projecturl',
            field=models.URLField(default='https://www.linkedin.com/in/ramrekha-yadav-4a8b21251/'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='img',
            field=models.ImageField(blank=True, default=0, null=True, upload_to='blog'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='title',
            field=models.CharField(default=0, max_length=250),
        ),
    ]
