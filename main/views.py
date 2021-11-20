from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Publication , Alerte , Commentaire
from django.contrib.auth.models import User
from django.contrib.auth import login , logout, authenticate
from django.contrib.auth.decorators import login_required
import os , datetime
from twilio.rest import Client
# Create your views here.

# fonction index 
def index(request):
    liste = User.objects.all()
    return render(request, "index.html", locals() )

def airProtege(request):
    return render(request, "air.html", locals())

def gestionnaire(request):
    return render(request, "gestionnaire.html", locals())

def departement(request):
    return render(request, "departement.html", locals())

def animauxProtege(request):
    return render(request, "animaux.html", locals())

def animalPartiel(request):
    return render(request, "partiel.html", locals())

def chasseInterdite(request):
    return render(request, "chasse.html", locals())

def Loi(request):
    return render(request, "lois.html", locals())

def delit(request):
    return render(request, "delits.html", locals())

def quizz(request):
    return render(request, "quizz.html", locals())

def forum(request):
    return render(request, "forum.html", locals())

# enregistrement d'un compte
def inscrir(request):
    data = request.POST
    
    if request.method == 'POST' :
        user = User.objects.create_user(
            username = data.get('pseudo'),
            email= data.get('email'),
            password= data.get('mdp'),
            first_name = data.get('prenom'),
            last_name = data.get('nom'),
        )
        user.save()

        message = "Utilisateurs enregistré avec succès"

    return redirect(index)

def alerte(request):
    return render(request, "alerte.html", locals())

# Enregistrer un alerte
def alerter(request):
    data = request.POST
    photo = request.FILES

    if request.method == 'POST' :
        alerte = Alerte.objects.create(
            photo = photo.get('photo'),
            description = data.get('description'),
            lieu = data.get('zone'),
            telephone = data.get('tel'),
        )
        alerte.save()
        #account_sid = os.environ['TWILIO_ACCOUNT_SID']
        account_sid = 'ACfd0eb2d9ceaed1a99ff52d94adb1ac96'
        #auth_token = os.environ['TWILIO_AUTH_TOKEN']
        auth_token = '797aa8ad29c84f94c2e86a0d3682ce39'
        twilio_client = Client(account_sid , auth_token)
        message = twilio_client.messages.create( to = '+242064362084', from_ = '+12054795793', body = data.get('description') )
        message.sid

    return redirect(index)


"""
# Modification d'un compte
def modificationCompte(request, id):
    import base64
    data = request.POST
    photo = request.FILES
    user = User.objects.get(id=id)

    if request.method == 'POST':
        user.username = data.get('pseudo', user.username)
        user.email = data.get('email', user.email)
        user.password = data.get('mdp', user.password)
        user.first_name = data.get('prenom', user.first_name)
        user.last_name = data.get('nom', user.last_name)
        
        compte.save()
        return redirect(home)

    else :
        mod = True
        return render(request, 'main/enregistrer.html', locals())

# Suppression du compte
def supprimer(request):
    data = request.POST
    if request.method == 'POST':
        id = data.get('id')

    user = User.objects.get(id=id)
    user.delete()

    return redirect(home)

#Connexion d'un utilisateur du forum
def connexion(request):
    data = request.POST
    user = authenticate(request,
        username = data.get('pseudo'),
        password = data.get('mdp'),
    )
    if user is not None :
        login(request, user)
        request.session['nom'] = user.username
        request.session['mdp'] = user.password
        return redirect(index)
    else :
        message = "Echec de la connexion"
        return render(request, 'mon_appli/connex.html', locals())

# verifier si l'utilisateur est conncté ou pas
def verificationConnexion(request) :
    if not request.user.is_authenticated :
        return redirect(home)
    else :
        return redirect()

#Deconnexion de l'utilisateur
def deconnexion(request):
    logout(request)
    return render(request, 'mon_appli/deconnex.html')

# Enregistrer une publication
@login_required(redirect_field_name = 'next!' , login_url = '/home/')
def publier(request):
    data = request.POST
    photo = request.FILES['photo']

    if request.method == 'POST' :
        post = Publication.objects.create(
            auteur = data.get('auteur')
            photo = photo,
            contenu = data.get('description'),
            categorie = data.get('phone'),
        )
        post.save()

    return redirect()

# Modifier une publication
@login_required(redirect_field_name = 'next!' , login_url = '/index/')
def modificationPublication(request, id):
    import base64
    data = request.POST
    photo = request.FILES
    post = Publication.objects.get(id=id)

    if request.method == 'POST':
        post.photo = data.get('photo', post.photo)
        post.contenu = data.get('contenu', post.contenu)
        post.categorie = data.get('categorie', post.categorie)

        post.save()
        return redirect(home)

    else :
        mod = True
        return render(request, 'templates/enregistrer.html', locals())

# Suppression une publication
def supprimer(request):
    data = request.POST
    if request.method == 'POST':
        id = data.get('id')

    post = Publication.objects.get(id=id)
    post.delete()
    return redirect(home)

# Enregistrer un commentaire
@login_required(redirect_field_name = 'next!' , login_url = '/index/')
def commenter(request):
    data = request.POST

    if request.method == 'POST' :
        comment = Commentaire.objects.create(
            auteur = data.get('auteur'),
            contenu = data.get('contenu'),
            post = data.get('post'),
        )
        comment.save()

    return redirect()

# Modifier un commentaire
@login_required(redirect_field_name = 'next!' , login_url = '/index/')
def modificationCommentaire(request, id):
    import base64
    data = request.POST
    photo = request.FILES
    comment = Commentaire.objects.get(id=id)

    if request.method == 'POST':
        comment.contenu = data.get('contenu', post.contenu)
        comment.post = data.get('post', comment.post)
        
        comment.save()
        return redirect(home)

    else :
        mod = True
        return render(request, 'main/enregistrer.html', locals())

# Supprimer un commentaire
def supprimer(request):
    data = request.POST
    if request.method == 'POST':
        id = data.get('id')

    comment = Commentaire.objects.get(id=id)
    comment.delete()
    return redirect(home)
"""