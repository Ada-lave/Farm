# Generated by Django 4.1.6 on 2023-03-15 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Earth', '0012_user_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcard',
            name='photo',
            field=models.ImageField(default=2, upload_to='product/img/'),
            preserve_default=False,
        ),
    ]
