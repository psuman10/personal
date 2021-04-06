from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm


urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>',views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart, name='pluscart'),
    path('minuscart/', views.minus_cart, name='minuscart'),
    path('removecart/', views.remove_cart, name='removecart'),
    path("search/", views.SearchView.as_view(), name="search"),

    path('Wears/', views.Wears, name='Wears'),
    path('Wears/<slug:data>', views.Wears, name='Wearsdata'),
    path('boot/', views.boot, name='boot'),
    path('boot/<slug:data>', views.boot, name='bootdata'),
    path('Halfface/', views.Halfface, name='Halfface'),
    path('Halfface/<slug:data>', views.Halfface, name='halfdata'),
    path('Fullface/', views.Fullface, name='Fullface'),
    path('Fullface/<slug:data>', views.Fullface, name='Fulldata'),
    path('deleteaddress/<int:id>/', views.delete_address, name='deleteaddress'),
    path('<int:id>/',views.update_address.as_view(),name="updateaddress"),
    path('profile1/', views.user_account, name='profile1'),
    path('paymentdone/', views.payment_done, name='paymentdone'),

    # path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('registration/', views.CustomerRegistrationView.as_view(),name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('login/', auth_views.LoginView.as_view(template_name='BC/login.html',authentication_form=LoginForm), name='login'),





    path('passwordchange/', auth_views.PasswordChangeView.as_view(
        template_name='BC/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(
        template_name='BC/passwordchangedone.html'), name='passwordchangedone'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='BC/password_reset.html',
                                                                 form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='BC/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='BC/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='BC/password_reset_complete.html'), name='password_reset_complete'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)