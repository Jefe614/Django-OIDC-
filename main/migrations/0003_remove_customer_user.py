# Generated by Django 4.2.14 on 2024-07-17 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_order_date_order_time_remove_customer_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]
