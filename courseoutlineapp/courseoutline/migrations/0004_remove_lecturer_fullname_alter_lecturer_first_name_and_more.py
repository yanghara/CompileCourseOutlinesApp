# Generated by Django 5.0.4 on 2024-06-15 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseoutline', '0003_lecturer_fullname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturer',
            name='fullname',
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='first_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='last_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
