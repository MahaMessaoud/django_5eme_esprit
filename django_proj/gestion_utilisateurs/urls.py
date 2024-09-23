# gestion_utilisateurs/urls.py
from django.urls import path
from .views import register_view, login_view, home_view  # Utilisez les noms exacts des fonctions dans views.py

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),  # Assurez-vous que le nom ici correspond à celui dans views.py
]
