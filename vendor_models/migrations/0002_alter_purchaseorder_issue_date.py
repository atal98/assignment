# Generated by Django 4.2.11 on 2024-04-29 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='issue_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
