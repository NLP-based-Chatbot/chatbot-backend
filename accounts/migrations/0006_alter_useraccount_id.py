# Generated by Django 3.2.7 on 2021-09-26 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210926_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
