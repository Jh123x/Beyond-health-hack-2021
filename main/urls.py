from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('register', views.register, name="register"),
    path('login', views.user_login, name="login"),
    path('logout', views.logout_view, name='logout'),
    path('about_us', views.about_us, name='about_us'),
    path('edit_profile', views.edit_profile, name="edit_profile"),
    path('donate', views.donations, name="donations"),
]