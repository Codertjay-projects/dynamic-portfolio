# Generated by Django 3.1.2 on 2021-09-10 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
        ('_profile', '0004_auto_20210910_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layout',
            name='portfolio_version',
            field=models.OneToOneField(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.portfoliotemplate'),
        ),
    ]
