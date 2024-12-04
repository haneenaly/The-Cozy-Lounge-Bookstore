from django.urls import path
from . import views

urlpatterns = [
    path('',views.store,name="store"),
    path('login/',views.loginPage,name='login'),
]