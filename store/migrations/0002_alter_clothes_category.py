# Generated by Django 4.1.5 on 2023-01-30 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='category',
            field=models.CharField(choices=[('dresses', 'dresses'), ('shirts', 'shirts'), ('jeans', 'jeans'), ('swimwear', 'swimwear'), ('sleepwear', 'sleepwear'), ('sportswear', 'sportswear'), ('jumpsuits', 'jumpsuits'), ('blazers', 'blazers'), ('jackets', 'jackets'), ('shoes', 'shoes')], max_length=20),
        ),
    ]