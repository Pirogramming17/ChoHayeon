# Generated by Django 4.0.6 on 2022-07-20 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devtool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='제목')),
                ('kind', models.CharField(max_length=50, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='제목')),
                ('user', models.CharField(max_length=50, verbose_name='유저이름')),
                ('content', models.TextField(verbose_name='내용')),
                ('interest', models.IntegerField(verbose_name='관심도')),
                ('image', models.ImageField(blank=True, upload_to='posts/%Y%m%d', verbose_name='사진')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('devtool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_devtool', to='posts.devtool')),
            ],
        ),
    ]
