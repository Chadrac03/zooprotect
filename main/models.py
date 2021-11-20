from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Alerte(models.Model) :
    photo = models.FileField("photo de la scène", upload_to="media/alerte", null=True)
    description = models.CharField("description alerte", max_length=70)
    lieu = models.CharField("lieu", max_length=90, null=True)
    telephone = models.CharField("telephone de la source", max_length=50)

class Categorie(models.Model):
    libelle = models.CharField("nom de la categorie", max_length=100)

class Publication(models.Model):
    auteur = models.ForeignKey(User, verbose_name="auteur de la publication", on_delete=models.CASCADE)
    titre = models.CharField("titre de la publication", max_length=50, null=True)
    photo = models.FileField("photo de la scène", upload_to="media/publication")
    contenu = models.TextField("contenu de la publication")
    categorie = models.ForeignKey(Categorie, verbose_name="categorie de la publication", on_delete=models.CASCADE)

class Commentaire(models.Model):
    auteur = models.ForeignKey(User, verbose_name="auteur du commentaire", on_delete=models.CASCADE)
    contenu = models.TextField("contenu du commentaire")
    post = models.ForeignKey(Publication, verbose_name="publication", on_delete=models.CASCADE)