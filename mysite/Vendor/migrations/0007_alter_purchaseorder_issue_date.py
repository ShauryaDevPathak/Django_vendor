# Generated by Django 4.2.6 on 2024-04-30 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0006_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='issue_date',
            field=models.DateTimeField(),
        ),
    ]
