# Generated by Django 2.2 on 2021-04-21 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_order_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='image',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='name',
            new_name='title',
        ),
    ]
