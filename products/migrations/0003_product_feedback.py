# Generated by Django 2.1.7 on 2019-03-15 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190315_0603'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='feedback',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]