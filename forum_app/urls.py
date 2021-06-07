"""rush01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import post_views, account_views, views

app_name = 'forum_app'

urlpatterns = [
    path('', post_views.PostView.as_view(), name='home'),
    path('login/', account_views.LogInView.as_view(), name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('registration/', views.registration, name='registration'),
    path('post/<int:post_id>', post_views.post, name='post'),
    path('post_create/', post_views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:post_id>/edit', post_views.PostEditView.as_view(), name='edit')
]
