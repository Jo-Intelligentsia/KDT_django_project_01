from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('profile/<user_pk>/', views.profile, name='profile')
]
