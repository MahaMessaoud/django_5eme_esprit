# gestion_utilisateurs/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import CustomUserCreationForm

# Vue pour l'inscription
def register_view(request):  # Assurez-vous que le nom est correct ici
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Inscription réussie ! Vous êtes maintenant connecté.")
            return redirect('home')
        else:
            messages.error(request, "Erreur lors de l'inscription. Veuillez vérifier les informations fournies.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Vue pour la connexion
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Connexion réussie !")
            return redirect('home')
        else:
            messages.error(request, "Veuillez entrer un nom d'utilisateur et un mot de passe corrects.")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# Vue pour la page d'accueil
def home_view(request):
    return render(request, 'home.html')
