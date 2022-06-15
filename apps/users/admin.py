from django.contrib import admin
from apps.users import models
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

admin.site.site_header = "Admin Panel"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Welcome Admin"
admin.site.unregister(Group)


@admin.action(description="Inactivate selected Users")
def make_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)


@admin.action(description="Activate selected Users")
def make_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    filter_horizontal = ["groups", "user_permissions"]
    list_display = [
        "email",
        "name",
        "is_staff",
        "is_superuser",
        "is_active",
    ]
    search_fields = ["email", "name"]
    list_filter = ["is_active", "is_staff", "is_superuser"]
    fieldsets = [
        ("Account", {"fields": ("email", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "name",
                    "user_type",
                    "phone",
                )
            },
        ),
        (
            "Permissions/Status",
            {"fields": ("is_staff", "is_superuser", "is_active")},
        ),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    ]
    actions = [make_inactive, make_active]
    ordering = ["email"]
    per_page = 20
