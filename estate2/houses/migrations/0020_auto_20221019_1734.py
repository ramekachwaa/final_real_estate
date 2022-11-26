# Generated by Django 3.2.14 on 2022-10-19 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0019_auto_20221019_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('location', models.CharField(choices=[('Ain Shokana', 'Ain Shokana'), ('Ain Sokhna', 'Ain Sokhna'), ('Alexandria', 'Alexandria'), ('East Cairo', 'East Cairo'), ('Mostakbal City', 'Mostakbal City'), ('New Cairo', 'New Cairo'), ('New Capital', 'New Capital'), ('North Coast', 'North Coast'), ('Sheik Zayed', 'Sheik Zayed'), ('West Cairo', 'West Cairo'), ('6th of October', '6th of October'), ('New Zayed', 'New Zayed')], default='Ain Shokana', max_length=500)),
                ('logo', models.ImageField(default='houses/real_estate_logo.jpg', upload_to='images')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='location',
            field=models.CharField(choices=[('Ain Shokana', 'Ain Shokana'), ('Ain Sokhna', 'Ain Sokhna'), ('Alexandria', 'Alexandria'), ('East Cairo', 'East Cairo'), ('Mostakbal City', 'Mostakbal City'), ('New Cairo', 'New Cairo'), ('New Capital', 'New Capital'), ('North Coast', 'North Coast'), ('Sheik Zayed', 'Sheik Zayed'), ('West Cairo', 'West Cairo'), ('6th of October', '6th of October'), ('New Zayed', 'New Zayed')], default='Ain Shokana', max_length=500),
        ),
        migrations.AddField(
            model_name='project',
            name='number_of_units',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('Any', 'Any'), ('Building', 'Building'), ('Clinic', 'Clinic'), ('Food & Beverage', 'Food & Beverage'), ('Office', 'Office'), ('Retail', 'Retail'), ('Shop', 'Shop'), ('Store', 'Store'), ('Apartment', 'Apartment'), ('Chalet', 'Chalet'), ('Condo', 'Condo'), ('Duplex', 'Duplex'), ('Ground Floor', 'Ground Floor'), ('iVilla', 'iVilla'), ('Multi Family Home', 'Multi Family Home'), ('Penthouse', 'Penthouse'), ('S Villa', 'S Villa'), ('Serviced Apartment', 'Serviced Apartment'), ('Single Family Home', 'Single Family Home'), ('Sky Loft', 'Sky Loft'), ('Studio', 'Studio'), ('Townhouse', 'Townhouse'), ('Twin House', 'Twin House'), ('Villa', 'Villa')], default='Apartment', max_length=50),
        ),
        migrations.AddField(
            model_name='project',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='houses.company'),
        ),
    ]
