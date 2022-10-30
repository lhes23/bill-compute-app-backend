# Generated by Django 4.1.2 on 2022-10-30 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reading', '0002_house_alter_reading_tenant_id_alter_reading_house_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='reading',
            name='bill',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reading',
            name='bill_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='reading',
            name='consumption',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reading',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='reading',
            name='due_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='reading',
            name='end_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='reading',
            name='paid_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reading',
            name='peso_per_consumption',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reading',
            name='present_reading',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reading',
            name='previous_reading',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reading',
            name='start_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='reading',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]