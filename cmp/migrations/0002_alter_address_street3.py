# Generated by Django 4.2.7 on 2023-11-12 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='street3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
