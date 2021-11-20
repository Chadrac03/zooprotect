# Generated by Django 3.2.9 on 2021-11-18 21:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commntaire',
            new_name='Commentaire',
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='auteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='auteur du commentaire'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='auteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='auteur de la publication'),
        ),
        migrations.DeleteModel(
            name='Utilisateur',
        ),
    ]
