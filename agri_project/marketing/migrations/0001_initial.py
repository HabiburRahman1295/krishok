# Generated by Django 5.2.1 on 2025-05-13 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('krishok_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('price_per_unit', models.FloatField()),
                ('seller_type', models.CharField(choices=[('wholesale', 'পাইকারী'), ('retail', 'খুচরা')], max_length=20)),
            ],
        ),
    ]
