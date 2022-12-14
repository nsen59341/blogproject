# Generated by Django 4.1.3 on 2022-12-01 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(default=0, max_length=36),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='title',
            field=models.CharField(default='test', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=64),
        ),
    ]
