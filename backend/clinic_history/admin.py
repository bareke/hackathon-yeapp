from django.contrib import admin
from .models import ClinicHistory

# Register your models here.


@admin.register(ClinicHistory)
class orderAdmin(admin.ModelAdmin):

    list_display = ('created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('created_at', 'updated_at')
