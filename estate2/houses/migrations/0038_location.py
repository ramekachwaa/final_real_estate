# Generated by Django 3.2.14 on 2022-11-29 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0037_merge_0025_auto_20221116_1920_0036_remove_code_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
