# Generated by Django 4.2 on 2024-12-04 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CribDashApp', '0003_contactinquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]
