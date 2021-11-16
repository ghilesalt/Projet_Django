from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'Api'

urlpatterns = [
    path('create-user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserView.as_view()),
    path('login/', views.SeConnecterView.as_view()),
    path('', TemplateView.as_view(
        template_name='doc.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]
