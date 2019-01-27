from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('api', views.api_root),
    path('api/restaurant', views.RestaurantList.as_view(), name='restaurant-list',),
    path('api/restaurant/<int:pk>/', views.RestaurantDetail.as_view()),
    path('api/cuisine_type/', views.CuisineTypeList.as_view(), name='cuisine_type-list',),
    path('api/outlet_type/', views.OutletTypeList.as_view(), name='outlet_type-list',),
    path('api/affordability/', views.AffordabilityList.as_view(), name='affordability-list',),
]

urlpatterns = format_suffix_patterns(urlpatterns)
