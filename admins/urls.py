from django.urls import path
from django.contrib.auth import views as auth_views


from admins import views

urlpatterns=[
    
    path('',views.admin_dashboard,name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('show-user',views.get_user),
    path('show-admin',views.get_admin),
    path('update-user-to-admin/<int:user_id>',views.update_user_to_admin),
    path('register-user',views.register_user_admin),
    path("admin-product/add/", views.AdminProductCreateView.as_view(),
         name="adminproductcreate"),
    path('deleteproduct/<int:id>/', views.delete_product, name='deleteproduct'),
    path('updateproduct<int:id>/',
         views.update_product.as_view(), name="updateproduct"),
    path('deleteorder/<int:id>/', views.delete_order, name='deleteorder'),
    path('deleteuser/<int:id>/', views.delete_user, name='deleteuser'),
    
]