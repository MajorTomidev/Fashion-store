# Generated by Django 4.1.5 on 2023-01-30 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('skirt', 'skirt'), ('gown', 'gown'), ('shirt', 'shirt'), ('t-shirt', 't-shirt'), ('trousers', 'trousers'), ('shorts', 'shorts')], max_length=20)),
                ('image', models.ImageField(default='fashion.jpg', upload_to='album_pictures')),
                ('price', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Clothes',
            },
        ),
    ]
