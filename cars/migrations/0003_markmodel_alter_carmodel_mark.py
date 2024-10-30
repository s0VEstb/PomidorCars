# Generated by Django 5.1.2 on 2024-10-30 16:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_carmodel_mark'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='mark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.markmodel'),
        ),
    ]