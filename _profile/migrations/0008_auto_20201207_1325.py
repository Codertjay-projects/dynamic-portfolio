# Generated by Django 3.1.2 on 2020-12-07 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_profile', '0007_auto_20201130_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='portfolio_version',
            field=models.CharField(choices=[('portfolio_v1', 'portfolio_v1'), ('portfolio_v2', 'portfolio_v2'), ('portfolio_v3', 'portfolio_v3'), ('portfolio_v4', 'portfolio_v4'), ('portfolio_v5', 'portfolio_v5')], default='portfolio_v1', max_length=20),
        ),
    ]