from django.urls import path
from . import views

app_name = 'aid_org'

urlpatterns = [
    path('aid_org/', views.aid_org, name='aid_org'),
]