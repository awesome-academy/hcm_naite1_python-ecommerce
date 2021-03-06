# Generated by Django 4.0.1 on 2022-02-16 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_remove_customer_user_customer_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.customer'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.customer'),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
