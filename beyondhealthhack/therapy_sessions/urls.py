from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='session page'),
    path("<int:path>", views.session, name="session")
]