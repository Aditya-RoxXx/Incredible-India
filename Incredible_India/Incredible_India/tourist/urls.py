from django.urls import path
from . import views

app_name = 'tourist'

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:city_id>/", views.detail, name="detail"),
    path("<int:city_id>/results/", views.results, name="results"),
    path("success/", views.success, name="success"),
    path("<int:city_id>/descriptions/", views.city_descriptions, name="city_descriptions")
]