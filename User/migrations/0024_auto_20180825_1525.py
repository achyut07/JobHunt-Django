# Generated by Django 2.0.6 on 2018-08-25 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0023_auto_20180825_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='Image',
            field=models.ImageField(blank=True, null='True', upload_to='mypics/%Y/%m/%d'),
        ),
    ]