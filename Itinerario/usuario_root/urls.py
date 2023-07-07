from django.urls import path, include
from usuarios import views

# libreria para ignorar el error
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
    # es para que no nos de error en el post cuando hacemos un post agregamos ese error al igual que el update porque tambieen hacemos post
    path("crear/", csrf_exempt(views.crear), name="crear"),
    path("login/", csrf_exempt(views.login), name="login"),
    path("delete/<int:id>", csrf_exempt(views.delete), name="delete"),

    
]