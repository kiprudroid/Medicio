from django.contrib import admin
from django.urls import path
from Blog import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home),
    path('inner', views.inner),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('upload/', views.upload, name='upload'),
    path('details/',views.detail, name='detail'),
    path('members/',views.members, name='members')
]
