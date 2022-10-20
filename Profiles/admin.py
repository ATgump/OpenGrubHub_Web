# from django.contrib import admin

# # Register your models here.
# # from .models import Profile

# # admin.site.register(Profile)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from django.contrib.auth.models import User

from .models import CustomerProfile, RestaurantProfile, User

# from django_google_maps import widgets as dgm_widgets
# from django_google_maps import fields as dgm_fields
import json


# ### THis is to update what admin can see in the users
class RestaurantProfileInline(admin.StackedInline):
    model = RestaurantProfile
    can_delete = False
    verbose_name_plural = "RestaurantProfile"
    fk_name = "user"
    # formfield_overrides = {
    #     dgm_fields.AddressField: {'widget':dgm_widgets.GoogleMapsAddressWidget(attrs=
    #         {'data-autocomplete-options': json.dumps({'types':['geocode','establishment'],'componentRestrictions':{'country':'us'}})}
    #     )},
    # }


# ### THis is to update what admin can see in the users
class ProfileInline(admin.StackedInline):
    model = CustomerProfile
    can_delete = False
    verbose_name_plural = "CustomerProfile"
    fk_name = "user"


class CustomUserAdmin(UserAdmin):
    inlines = (
        ProfileInline,
        RestaurantProfileInline,
    )
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "get_birth_date",
        "get_address",
        "get_id",
        "get_customer_status",
    )
    list_select_related = (
        "customer_profile",
        "restaurant_profile",
    )
    # list_editable=('email',)
    # actions=['authorize_selected',"role_change_exec"]

    # @admin.action(description="Authorize Member")
    # def authorize_selected(modeladmin,request,queryset):
    #     #print(queryset.values('id'))
    #     for userid in queryset.values('id'):
    #         user = User.objects.get(pk=userid["id"])
    #         user.profile.role=2
    #         user.save()
    # @admin.action(description="Make Executive")
    # def role_change_exec(modeladmin,request,queryset):
    #     #print(queryset.values('id'))
    #     for userid in queryset.values('id'):
    #         user = User.objects.get(pk=userid["id"])
    #         user.profile.role=3
    #         user.save()
    #     #queryset.update(profile=2)
    def get_birth_date(self, instance):
        return instance.customer_profile.date_of_birth

    get_birth_date.short_description = "Birth Date"

    def get_address(self, instance):
        return instance.restaurant_profile.restaurant_address

    get_address.short_description = "address"

    def get_id(self, instance):
        return instance.id

    get_id.short_description = "id"

    def get_customer_status(self, instance):
        return instance.is_customer
    get_customer_status.short_description = "Customer Status"

    # def get_role(self, instance):
    #     return instance.profile.role
    # get_role.short_description = 'Role'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.register(User, CustomUserAdmin)
# admin.site.register(User, CustomUserAdmin)
