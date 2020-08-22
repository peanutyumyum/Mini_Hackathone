# Generated by Django 3.1 on 2020-08-22 06:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=2000)),
                ('author', models.CharField(max_length=100)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('hit', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment_contents', models.CharField(max_length=200)),
                ('comment_writer', models.CharField(max_length=100)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='community.blog')),
            ],
        ),
    ]
