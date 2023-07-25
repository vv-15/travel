from . import views
from django.urls import path

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
    #path('add/',views.addition,name='addition')
    #path('sub/',views.subtraction,name='subtraction'),
    #path('mul/',views.multiplication,name='multiplication'),
    #path('div/',views.division,name='division')

]