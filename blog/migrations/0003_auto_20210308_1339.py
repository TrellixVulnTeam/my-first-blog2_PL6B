# Generated by Django 2.2.19 on 2021-03-08 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_commnet'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commnet',
            new_name='Comment',
        ),
    ]