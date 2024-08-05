# Generated by Django 5.0.6 on 2024-08-04 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0004_blog_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
