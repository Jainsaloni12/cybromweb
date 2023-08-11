# Generated by Django 4.2 on 2023-06-22 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_servicerelated'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionSix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=100)),
                ('client_image', models.ImageField(upload_to='images_clients')),
                ('client_name', models.CharField(max_length=40)),
                ('profession', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='servicerelated',
            name='full_desc',
            field=models.TextField(),
        ),
    ]