from django.urls import path
from . import views, controllers

# for namespacing
app_name = 'shop'

urlpatterns = [
    # views
    path('',views.shop, name='index'),
    path('shop',views.shop, name='shop'),
    path('wishlist',views.wishlist, name='wishlist'),
    path('cart',views.cart, name='cart'),
    path('checkout',views.checkout, name='checkout'),
    path('my-account',views.my_account, name='my-account'),

    # controllers
    path('add_to_wishlist/<int:id>', controllers.add_to_wishlist, name="add-to-wishlist"),
    path('delete_from_wishlist/<int:id>', controllers.delete_from_wishlist, name="delete-from-wishlist"),
    path('add_to_cart/<int:id>', controllers.add_to_cart, name="add-to-cart"),
    path('update_cart', controllers.update_cart, name="update-cart"),
    path('delete_from_cart/<int:id>', controllers.delete_from_cart, name="delete-from-cart"),
    path('login', controllers.user_login, name="login"),
    path('logout', controllers.user_logout, name="logout"),
    path('register', controllers.user_register, name="register")
]

# TODO: look page 37 for template namespacing
# TODO: look page 606 for managing js,css file