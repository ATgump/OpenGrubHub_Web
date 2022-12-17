
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomerProfile, RestaurantProfile, User

# ### This is to update what admin can see in the users
class RestaurantProfileInline(admin.StackedInline):
    model = RestaurantProfile
    can_delete = False
    verbose_name_plural = "RestaurantProfile"
    fk_name = "user"

# ### This is to update what admin can see in the users
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
    ## Display these fields for a user to admin
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "get_birth_date",
        "get_address",
        "get_id",
        "get_restaurant_name",
        "get_restaurant_lat",
        "get_restaurant_long",
        "get_customer_status",
        "get_password",
    )
    list_select_related = (
        "customer_profile",
        "restaurant_profile",
    )
    ## Inlines to display model fields in admin section
    def get_birth_date(self, instance):
        return instance.customer_profile.date_of_birth
    get_birth_date.short_description = "Birth Date"

    def get_restaurant_name(self, instance):
        return instance.restaurant_profile.restaurant_name
    get_restaurant_name.short_description = "Restaurant Name"

    def get_address(self, instance):
        return instance.restaurant_profile.restaurant_address
    get_address.short_description = "address"

    def get_restaurant_lat(self, instance):
        return instance.restaurant_profile.lat
    get_restaurant_lat.short_description = "Restaurant lat"

    def get_restaurant_long(self, instance):
        return instance.restaurant_profile.long
    get_restaurant_long.short_description = "Restaurant long"

    def get_id(self, instance):
        return instance.id
    get_id.short_description = "id"

    def get_customer_status(self, instance):
        return instance.is_customer
    get_customer_status.short_description = "Customer Status"

    def get_password(self, instance):
        return instance.password
    get_password.short_description = "Password"

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

## Finally register the model
admin.site.register(User, CustomUserAdmin)

