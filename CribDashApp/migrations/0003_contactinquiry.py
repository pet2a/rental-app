# Generated by Django 4.2 on 2024-12-02 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CribDashApp', '0002_delete_property_alter_properties_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('message', models.TextField()),
                ('agent_name', models.CharField(max_length=100)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
