# Generated by Django 4.1.4 on 2022-12-15 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usemodel',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=6),
        ),
    ]
