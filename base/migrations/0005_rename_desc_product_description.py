# Generated by Django 4.0.6 on 2023-05-29 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_proddesc_product_desc_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='desc',
            new_name='description',
        ),
    ]