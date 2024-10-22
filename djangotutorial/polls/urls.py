from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),  # URL para el detalle de la pregunta
]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
