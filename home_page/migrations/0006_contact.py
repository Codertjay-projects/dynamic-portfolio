# Generated by Django 3.1.2 on 2021-07-31 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0005_subscribeuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
