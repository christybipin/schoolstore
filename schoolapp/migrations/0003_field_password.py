# Generated by Django 5.0 on 2023-12-30 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0002_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='password',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
