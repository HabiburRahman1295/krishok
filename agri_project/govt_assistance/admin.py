from django.contrib import admin
from .models import AssistanceApplication

@admin.register(AssistanceApplication)
class AssistanceAdmin(admin.ModelAdmin):
    list_display = ('krishok_name', 'phone', 'assistance_type', 'submitted_at')
    list_filter = ('assistance_type',)
    search_fields = ('krishok_name', 'phone')
