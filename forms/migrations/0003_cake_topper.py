# Generated by Django 4.0.4 on 2022-05-04 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_contactphotos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=400, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=400, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
