# Generated by Django 5.0.6 on 2024-06-13 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('order', models.CharField(max_length=32)),
                ('review', models.CharField(max_length=50)),
                ('conneection', models.ManyToManyField(to='restaurant.restaurant')),
            ],
        ),
    ]
