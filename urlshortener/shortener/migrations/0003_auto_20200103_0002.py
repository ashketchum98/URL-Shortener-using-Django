# Generated by Django 2.1.7 on 2020-01-02 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20200102_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]
