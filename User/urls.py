from django.contrib import admin
from django.urls import path
from User import views
app_name = 'User'
urlpatterns = [

    path('base/',views.base,name='base'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login_user/',views.login_user,name='login_user'),
    path('logout/',views.logout,name='logout'),
    path('company/',views.company,name='company'),
    path('profile/',views.profile,name='profile'),
    path('postjob/',views.postjob,name='postjob'),
    path('choose/',views.choose,name='choose'),
    path('apply/',views.apply,name='apply'),
    # path('search/',views.search,name='search')
    # path('logout_user/', views.logout_user, name='logout_user'),
] 