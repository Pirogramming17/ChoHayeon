# Generated by Django 4.0.6 on 2022-07-20 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devtool',
            name='kind',
            field=models.CharField(max_length=50, verbose_name='종류'),
        ),
        migrations.AlterField(
            model_name='devtool',
            name='name',
            field=models.CharField(max_length=50, verbose_name='이름'),
        ),
    ]
