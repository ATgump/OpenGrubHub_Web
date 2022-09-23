from django.contrib import admin

# Register your models here.
# from .models import Profile

# admin.site.register(Profile)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile







### THis is to update what admin can see in the users
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_birth_date','get_role')
    list_select_related = ('profile', )
    #list_editable=('email',)
    actions=['authorize_selected',"role_change_exec"]


    @admin.action(description="Authorize Member")
    def authorize_selected(modeladmin,request,queryset):
        #print(queryset.values('id'))
        for userid in queryset.values('id'):
            user = User.objects.get(pk=userid["id"])
            user.profile.role=2
            user.save()
    @admin.action(description="Make Executive")
    def role_change_exec(modeladmin,request,queryset):
        #print(queryset.values('id'))
        for userid in queryset.values('id'):
            user = User.objects.get(pk=userid["id"])
            user.profile.role=3
            user.save()
        #queryset.update(profile=2)
    def get_birth_date(self, instance):
        return instance.profile.birth_date
    get_birth_date.short_description = 'Birth Date'

    def get_role(self, instance):
        return instance.profile.role
    get_role.short_description = 'Role'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)