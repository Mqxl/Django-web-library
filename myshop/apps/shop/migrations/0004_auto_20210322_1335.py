# Generated by Django 3.1.7 on 2021-03-22 07:35

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210321_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(db_index=True, max_length=200, verbose_name=shop.models.Urok),
        ),
    ]