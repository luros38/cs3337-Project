from django.urls import path
from . import views


urlpatterns = [

    path("", views.index, name="index"),
    path("aboutus/", views.about_us, name="about_us"),
    path("book_detail/<int:book_id>", views.book_detail, name="book_detail"),
    path("book_delete/<int:book_id>", views.book_delete, name="book_delete"),
    path("postbook", views.postbook, name="postbook"),
    path("post_success", views.post_success, name="post_success"),
    path("displaybooks", views.displaybooks, name="displaybooks"),
    path("mybooks", views.mybooks, name="mybooks"),
    path('add_comment/<int:book_id>/', views.add_comment, name='add_comment'),
    path('displaycom/<int:book_id>/', views.displaycom, name='displaycom'),
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:book_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart, name='cart'),
    path('search', views.search_book, name='search_book'),
    path('my_favorites/', views.my_favorites, name='my_favorites'),
    path('favorite/<int:book_id>/', views.favorite, name='favorite'),
    path('remove_favorite/<int:book_id>/', views.remove_favorite, name='remove_favorite'),
    path('update_cart/', views.update_cart, name='update_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order_success/', views.order_success, name='order_success'),
    path('cancel_cart/', views.cancel_cart, name='cancel_cart'),


]
