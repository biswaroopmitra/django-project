"""learning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from .views import CityListCreateView, CityDetailView, CityDetailByNameView

urlpatterns = [
    # List and Create endpoints
    path('cities/', CityListCreateView.as_view(), name='city-list-create'),
    
    # View by name endpoint
    path('cities/by-name/', CityDetailByNameView.as_view(), name='city-detail-by-name'),
    
    # Detail endpoints (retrieve, update, delete)
    path('cities/<int:city_id>/', CityDetailView.as_view(), name='city-detail'),
]
