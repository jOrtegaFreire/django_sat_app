# Generated by Django 4.1.2 on 2022-10-31 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_email',
            field=models.CharField(default='NaN', max_length=32),
            preserve_default=False,
        ),
    ]
