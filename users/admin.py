from django.db import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Club

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            "Profile",
            {
                "fields": (
                    "name",
                    "email",
                    "belongs"
                ),
                "classes": ("wide",),
            },
        ),
        (
            "Important Dates",
            {
                "fields": ("last_login", "date_joined"),
                "classes": ("collapse",),
            },
        ),
    )

    list_display = ("username", "email", "name","total_clubs")

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    
    list_display = (
        "name",
        "description"
    )
    
    readonly_fields = (
        "created_at",
        "updated_at",
    )
