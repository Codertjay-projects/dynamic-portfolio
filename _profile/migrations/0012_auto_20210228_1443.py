# Generated by Django 3.1.2 on 2021-02-28 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0002_auto_20210228_1427'),
        ('_profile', '0011_auto_20210130_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='portfolio_version',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home_page.portfoliotemplate'),
        ),
    ]