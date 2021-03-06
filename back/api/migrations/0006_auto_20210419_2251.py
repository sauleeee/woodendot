# Generated by Django 2.2 on 2021-04-19 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210419_2158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='furniture',
            old_name='description',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='furniture',
            old_name='description2',
            new_name='body2',
        ),
        migrations.RenameField(
            model_name='furniture',
            old_name='description3',
            new_name='body3',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='body',
        ),
        migrations.AlterField(
            model_name='furniture',
            name='img',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='img2',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='img3',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='img4',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='price',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.CharField(max_length=200),
        ),
    ]
