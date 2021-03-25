from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>',views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),

    path('Wears/', views.Wears, name='Wears'),
    path('Wears/<slug:data>', views.Wears, name='Wearsdata'),
    path('boot/', views.boot, name='boot'),
    path('boot/<slug:data>', views.boot, name='bootdata'),
    path('Halfface/', views.Halfface, name='Halfface'),
    path('Halfface/<slug:data>', views.Halfface, name='halfdata'),
    path('Fullface/', views.Fullface, name='Fullface'),
    path('Fullface/<slug:data>', views.Fullface, name='Fulldata'),

    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('login/', views.login, name='login'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)