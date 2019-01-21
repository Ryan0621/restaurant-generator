from django.contrib import admin
from .models import Restaurant, OpeningTime, OutletType, Affordability, CuisineType
from address.models import AddressField
from address.forms import AddressWidget

# Register your models here.
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'address',
        'outlet_type',
        'cuisine_type',
        'affordability',
        'vegan_friendly',
        'halal'
    )

    formfield_overrides = {
        AddressField: {
            'widget': AddressWidget(
                attrs={
                    'style': 'width: 300px;'
                }
            )
        }
}

@admin.register(OutletType)
class OutletTypeAdmin(admin.ModelAdmin):

    list_display = ('id', 'outlet_type')

admin.site.register(CuisineType)
admin.site.register(OpeningTime)
admin.site.register(Affordability)
