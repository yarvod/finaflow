from django.contrib import admin


class BaseUserAdmin(admin.ModelAdmin):
    list_display = ("get_username", "get_first_name", "get_last_name")

    @admin.display(ordering="user__email", description="Email")
    def get_username(self, obj):
        return obj.user.email

    @admin.display(ordering="user__first_name", description="First Name")
    def get_first_name(self, obj):
        return obj.user.first_name

    @admin.display(ordering="user__last_name", description="Second Name")
    def get_last_name(self, obj):
        return obj.user.last_name

    class Meta:
        abstract = True
