from django.urls import path
from . import views

app_name = 'election'

urlpatterns = [
    path('', views.login, name='login'),      # หน้าแรกคือ login
    path('home/', views.home, name='home'),        # หน้าโหวต
    path('vote/<int:candidate_id>/', views.vote, name='vote'),
]