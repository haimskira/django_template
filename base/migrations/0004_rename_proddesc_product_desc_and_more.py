# Generated by Django 4.0.6 on 2023-05-29 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='proddesc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='prodname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='prodprice',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='prodsize',
            new_name='size',
        ),
    ]