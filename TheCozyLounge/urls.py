from django.urls import path
from . import views

urlpatterns = [
    path('',views.store,name="store"),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerPage,name='register'),
    path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    path('AboutUs/', views.about_us, name='about_us'),
    path('product/<int:product_id>/', views.details_view, name='view'),
    path ('search/',views.search_view,name="search"),
]