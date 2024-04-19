from django.urls import path
from userapp import views
urlpatterns = [

path('',views.user,name='user'),
path('login/',views.login,name='login'),
path('logout/',views.logout,name='logout'),
path('forgotpassword',views.forgotpassword,name='forgotpassword')
]