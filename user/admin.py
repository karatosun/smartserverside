from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.



class MyUserAdmin(UserAdmin):
    list_display =  ('id',) + UserAdmin.list_display
    list_display_links = ['first_name', 'last_name', "username", 'email']

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)