# Generated by Django 3.0.6 on 2020-05-30 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='patient',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='case',
            name='receptionist',
            field=models.CharField(max_length=250),
        ),
    ]
