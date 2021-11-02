# Generated by Django 3.2.6 on 2021-11-01 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_product_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='label',
            field=models.CharField(choices=[('O', 'Out of stock'), ('N', 'New'), ('S', 'Selling Fast')], default=False, max_length=1, null=True),
        ),
    ]