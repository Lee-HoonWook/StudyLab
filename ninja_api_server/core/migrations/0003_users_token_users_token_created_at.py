# Generated by Django 4.2.2 on 2023-06-13 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='token',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='token_created_at',
            field=models.DateTimeField(null=True),
        ),
    ]
