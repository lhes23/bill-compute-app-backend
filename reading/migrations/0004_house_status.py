# Generated by Django 4.1.2 on 2022-10-30 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reading', '0003_reading_bill_reading_bill_type_reading_consumption_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='status',
            field=models.CharField(blank=True, default='vacant', max_length=255),
        ),
    ]
