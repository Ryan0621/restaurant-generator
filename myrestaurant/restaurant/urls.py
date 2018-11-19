from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.api_root),
    path('restaurant/', views.RestaurantList.as_view(), name='restaurant-list',),
    path('restaurant/<int:pk>/', views.RestaurantDetail.as_view()),
    path('cuisine_type/', views.CuisineTypeList.as_view(), name='cuisine_type-list',),
    path('outlet_type/', views.OutletTypeList.as_view(), name='outlet_type-list',),
    path('affordability/', views.AffordabilityList.as_view(), name='affordability-list',),
]

urlpatterns = format_suffix_patterns(urlpatterns)
