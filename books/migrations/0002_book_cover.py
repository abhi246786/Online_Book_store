# Generated by Django 2.2.9 on 2020-02-05 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]