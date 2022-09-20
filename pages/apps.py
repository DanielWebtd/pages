# Esto es de Django.
from django.apps import AppConfig


# PagesConfig es el nombre que se usa en el
# proyecto principal (django_project.settings.INSTALLED_APPS)
class PagesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "pages"
