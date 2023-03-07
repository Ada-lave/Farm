# Generated by Django 4.1.7 on 2023-03-04 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Earth', '0009_alter_profileuser_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='VegetableCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(max_length=1000)),
                ('photo', models.ImageField(upload_to='')),
                ('data_of_pick', models.DateField()),
                ('price', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Earth.profileuser')),
            ],
        ),
    ]