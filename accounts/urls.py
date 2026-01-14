from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('',views.dashboard, name='dashboard'),
    
    path('activate/<uidb64>/<token>/',views.activate,name='activate'),
    path('forgotPassword/',views.forgotPassword,name='forgotPassword'),
    path('resetpassword_validation/<uidb64>/<token>/',views.resetpassword_validation,name='resetpassword_validation'),
     path('resetPassword/',views.resetPassword,name='resetPassword'),
]
