from django.contrib import admin
from .models import Restaurant, OpeningTime, OutletType, Affordability, CuisineType

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(OutletType)
admin.site.register(CuisineType)
admin.site.register(OpeningTime)
admin.site.register(Affordability)
