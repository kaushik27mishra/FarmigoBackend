from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import *

class BaseUserAdmin(UserAdmin):
    add_form = BaseUserCreationForm
    form = BaseUserChangeForm
    model = BaseUser
    list_display = ('user_type', 'username', 'email')
    UserAdmin.add_fieldsets = (
        (None, {
            'fields': ('user_type', 'username', 'password', 'email')
        }),
    )
    UserAdmin.fieldsets = (
        (None, { 'fields': ('username', 'email')
        }),
    )

admin.site.register(BaseUser, BaseUserAdmin)

admin.site.register(Farmer)
admin.site.register(Crop)
admin.site.register(FarmerProduct)
admin.site.register(Livestock)

admin.site.register(Retailer)
admin.site.register(RetailerProduct)

admin.site.register(Supplier)
admin.site.register(SupplierProduct)
