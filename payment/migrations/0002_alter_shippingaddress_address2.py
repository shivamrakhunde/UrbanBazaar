# Generated by Django 5.1.1 on 2024-10-11 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='address2',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
