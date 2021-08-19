# Generated by Django 3.1.2 on 2021-07-31 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectitem',
            name='project',
        ),
        migrations.RemoveField(
            model_name='projectitem',
            name='user',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='user',
        ),
        migrations.RemoveField(
            model_name='service',
            name='user',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='user',
        ),
        migrations.RemoveField(
            model_name='testimonial',
            name='user',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='ProjectItem',
        ),
        migrations.DeleteModel(
            name='Resume',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='Skills',
        ),
        migrations.DeleteModel(
            name='Testimonial',
        ),
    ]