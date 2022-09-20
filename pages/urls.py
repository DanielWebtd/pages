# Esto es de Django
from django.urls import path

# Esta es mi vista.
from .views import AboutPageView, HomePageView

urlpatterns = [
    # Cuando usamos Class-Based Views
    # siempre debes agregar as_view() al final
    # del nombre de vista
    path("about", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
]
