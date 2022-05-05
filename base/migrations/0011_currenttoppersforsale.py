# Generated by Django 4.0.4 on 2022-05-03 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_topperspageadditionalimages_topperspageinitialimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentToppersForSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, null=True)),
                ('Cost', models.TextField(help_text='Numbers only please with two decimals! ex 13.95', max_length=400, null=True)),
                ('Image', models.ImageField(default='temp.png', null=True, upload_to='')),
                ('Esty_Link', models.TextField(max_length=400, null=True)),
            ],
        ),
    ]
