# Generated by Django 4.2 on 2023-06-15 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_aboutcybrom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('mobile_no', models.BigIntegerField()),
                ('query', models.TextField()),
            ],
        ),
    ]
