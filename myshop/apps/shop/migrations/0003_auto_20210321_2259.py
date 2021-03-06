# Generated by Django 3.1.7 on 2021-03-21 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210321_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='urok3', to='shop.urok', to_field='name'),
        ),
        migrations.AlterField(
            model_name='urok',
            name='name',
            field=models.CharField(db_index=True, max_length=200, unique=True),
        ),
    ]
