# Generated by Django 4.2 on 2024-12-02 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CribDashApp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Property',
        ),
        migrations.AlterModelOptions(
            name='properties',
            options={},
        ),
        migrations.RemoveField(
            model_name='properties',
            name='date_posted',
        ),
        migrations.RemoveField(
            model_name='properties',
            name='square_footage',
        ),
    ]
