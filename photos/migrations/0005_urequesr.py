# Generated by Django 4.2.1 on 2023-05-23 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='urequesr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('msg', models.CharField(max_length=500)),
                ('insta', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
