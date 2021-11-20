from django.contrib import admin
from django.urls import path
from main.views import *
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', index, name="racine"),
    path('aire&protege', airProtege, name="ap"),
    path('gestionnaire', gestionnaire, name="gestionnaire"),
    path('departement', departement, name="departement"),
    path('animaux/protege', animauxProtege, name="animaux"),
    path('animaux/partiellement/protege', animalPartiel, name="partielanimal"),
    path('animaux&totalement&protege', animauxProtege, name="totalanimal"),
    path('techniques/methodes/chasse/interdites', chasseInterdite, name="chasse"),
    path('les/lois', Loi, name="loi"),
    path('les/delits', delit, name="delit"),
    path('les/quizz', quizz, name="quizz"),
    path('Alerte/Alerte', alerte, name="twilio"),
    path(' ', alerter, name="generer"),
    path('forum/zooprotect', forum, name="forum"),
    path('creercompte', inscrir, name="creerCompte"),
    path('login/', auth_view.LoginView.as_view()),
]
