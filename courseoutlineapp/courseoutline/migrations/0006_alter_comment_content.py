# Generated by Django 5.0.4 on 2024-05-15 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseoutline', '0005_alter_course_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=255),
        ),
    ]