# Generated by Django 3.1.2 on 2020-11-14 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20201114_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100, verbose_name='URL')),
                ('order_owner', models.CharField(max_length=200, verbose_name='Клиент')),
                ('qr_code', models.ImageField(blank=True, upload_to='qr_codes', verbose_name='QR-код')),
            ],
        ),
        migrations.DeleteModel(
            name='Website',
        ),
    ]