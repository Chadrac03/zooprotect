# Generated by Django 3.2.9 on 2021-11-19 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211119_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alerte',
            name='date',
        ),
        migrations.AlterField(
            model_name='alerte',
            name='photo',
            field=models.FileField(null=True, upload_to='media/alerte', verbose_name='photo de la scène'),
        ),
    ]
