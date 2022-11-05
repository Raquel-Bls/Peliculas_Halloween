from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUser, CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    auth_form = CustomUserCreationForm
    model = CustomUser
    form = CustomUserChangeForm
    list_display = ['is_staff', 'username',
                    'email', 'Nombre', 'Apellido', 'Edad']


admin.site.register(CustomUser, CustomUserAdmin)
