# Generated by Django 4.2.6 on 2024-04-30 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0004_purchaseorder_acknowledgment_date_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PurchaseOrder',
        ),
        migrations.DeleteModel(
            name='Vendor',
        ),
    ]
