from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from .models import Memory, Userpic, Coordinates


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username", ]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Userpic)
admin.site.register(Memory)
admin.site.register(Coordinates)
