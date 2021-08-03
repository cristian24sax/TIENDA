from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('table/',views.table,name='table'),
    path('404/',views.error,name='404'),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('login/',views.login_page,name='login'),
    path('register/',views.register_page,name='register'),
    path('logout/',views.logout_user,name='logout'),
    path('SinPrivilegios/',views.HomeSinPrivilegios,name='SinPrivilegios'),
]