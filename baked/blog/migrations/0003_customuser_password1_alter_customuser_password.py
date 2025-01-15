# Generated by Django 5.1.3 on 2024-12-30 02:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_customuser_alter_usercommentmodel_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='password1',
            field=models.CharField(default=False, max_length=150, validators=[django.core.validators.MinLengthValidator(8)], verbose_name='Hasło:'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
