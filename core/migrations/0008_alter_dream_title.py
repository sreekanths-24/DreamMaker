# Generated by Django 3.2.24 on 2024-03-31 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20240303_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dream',
            name='title',
            field=models.CharField(max_length=800),
        ),
    ]