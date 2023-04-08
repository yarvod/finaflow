from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import Group

from .models import User, CustomGroup

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(CustomGroup, BaseGroupAdmin)
