# Generated by Django 5.0.4 on 2024-05-26 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseoutline', '0002_outline_image_outline_is_approved_alter_account_role_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer',
            name='fullname',
            field=models.CharField(editable=False, max_length=510, null=True),
        ),
    ]
