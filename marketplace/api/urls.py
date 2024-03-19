from django.urls import path
from api import views

urlpatterns = [
    path('marketplace/',
         views.MarketplaceViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('marketplace/<int:pk>/', views.MarketplaceViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
