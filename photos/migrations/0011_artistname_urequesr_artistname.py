# Generated by Django 4.2.1 on 2023-05-27 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0010_customer_order_shippingaddress_orderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='artistname',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='urequesr',
            name='artistname',
            field=models.CharField(default='Any Artist', max_length=100),
        ),
    ]
