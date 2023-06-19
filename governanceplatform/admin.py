from django import forms
from django.contrib import admin
from django.contrib.auth.models import Permission
from django.utils.translation import gettext_lazy as _
from django_otp import devices_for_user
from django_otp.decorators import otp_required
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin

from governanceplatform.models import User
from governanceplatform.settings import SITE_NAME


# Customize the admin site
class CustomAdminSite(admin.AdminSite):
    site_header = SITE_NAME + " " + _("Administration")
    site_title = SITE_NAME

    def admin_view(self, view, cacheable=False):
        decorated_view = otp_required(view)
        return super().admin_view(decorated_view, cacheable)


admin_site = CustomAdminSite()


class UserResource(resources.ModelResource):
    id = fields.Field(column_name="id", attribute="id")
    first_name = fields.Field(column_name="first_name", attribute="first_name")
    last_name = fields.Field(column_name="last_name", attribute="last_name")
    email = fields.Field(column_name="email", attribute="email")
    phone_number = fields.Field(column_name="phone_number", attribute="phone_number")

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
        ]


# reset the 2FA we delete the TOTP devices
@admin.action(description=_("Reset 2FA"))
def reset_2FA(modeladmin, request, queryset):
    for user in queryset:
        devices = devices_for_user(user)
        for device in devices:
            device.delete()


@admin.register(User, site=admin_site)
class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = UserResource
    list_display = [
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "is_superuser",
        "is_staff",
    ]
    search_fields = ["first_name", "last_name", "email"]
    list_filter = [
        "is_staff",
    ]
    list_display_links = ("email", "first_name", "last_name")
    filter_horizontal = ("groups",)
    fieldsets = [
        (
            _("Contact Information"),
            {
                "classes": ["extrapretty"],
                "fields": [
                    ("first_name", "last_name"),
                    ("email", "phone_number"),
                ],
            },
        ),
        (
            _("Permissions"),
            {
                "classes": ["extrapretty"],
                "fields": [
                    "is_superuser",
                    "is_staff",
                ],
            },
        ),
        # (
        #     "Group Permissions",
        #     {"classes": ("collapse",), "fields": ("groups", "user_permissions")},
        # ),
    ]
    actions = [reset_2FA]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        return form

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset

        # if request.user.has_perms(
        #     [
        #         "governanceplatform.add_user",
        #         "governanceplatform.change_user",
        #         "governanceplatform.delete_user",
        #     ],
        # ):
        #     return queryset.filter(
        #         sectors__in=request.user.sectors.filter(
        #             sectoradministration__is_sector_administrator=True
        #         ),
        #         companies__in=request.user.companies.all(),
        #     ).distinct()
        return queryset.exclude(email=request.user.email)

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            super().save_model(request, obj, form, change)            
        else:
            if obj.id is None and obj.is_staff:
                super().save_model(request, obj, form, change)
                obj.user_permissions.add(
                    Permission.objects.get(codename="add_user"),
                    Permission.objects.get(codename="change_user"),
                    Permission.objects.get(codename="delete_user"),
                )
            super().save_model(request, obj, form, change)
