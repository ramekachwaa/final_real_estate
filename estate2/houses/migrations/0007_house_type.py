# Generated by Django 3.2.14 on 2022-10-12 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0006_auto_20221012_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='type',
            field=models.CharField(choices=[('Any', 'Any'), ('Building', 'Building'), ('clinic', 'clinic'), ('Food & Beverage', 'Food & Beverage'), ('Office', 'Office'), ('Retail', 'Retail'), ('Shop', 'Shop'), ('Store', 'Store'), ('Apartment', 'Apartment'), ('Chalet', 'Chalet'), ('Condo', 'Condo'), ('Duplex', 'Duplex'), ('Ground Floor', 'Ground Floor'), ('iVilla', 'iVilla'), ('Multi Family Home', 'Multi Family Home'), ('Penthouse', 'Penthouse'), ('S Villa', 'S Villa'), ('Serviced Apartment', 'Serviced Apartment'), ('Single Family Home', 'Single Family Home'), ('Sky Loft', 'Sky Loft'), ('Studio', 'Studio'), ('Townhouse', 'Townhouse'), ('Twin House', 'Twin House'), ('Villa', 'Villa')], default='Apartment', max_length=50),
        ),
    ]