# Generated by Django 5.0.4 on 2024-04-30 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_API_Produtos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
    ]
