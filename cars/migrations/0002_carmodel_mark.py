# Generated by Django 5.1.2 on 2024-10-30 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='mark',
            field=models.CharField(default='mark', max_length=255),
            preserve_default=False,
        ),
    ]
