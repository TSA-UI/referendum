# Generated by Django 5.1.1 on 2024-10-23 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_alter_reviewentry_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewentry',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
