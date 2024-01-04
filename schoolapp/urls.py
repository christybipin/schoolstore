from django.urls import path

from . import views

urlpatterns = [

    path('', views.store, name="store"),
    path('register/', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('click_view/', views.click_view, name="click_view"),
    path('add_form/', views.add_form, name="add_form"),

]
