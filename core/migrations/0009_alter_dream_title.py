# Generated by Django 3.2.25 on 2024-04-11 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_dream_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dream',
            name='title',
            field=models.TextField(),
        ),
    ]