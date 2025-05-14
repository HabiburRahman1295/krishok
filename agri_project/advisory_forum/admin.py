from django.contrib import admin
from .models import Advisory

@admin.register(Advisory)
class AdvisoryAdmin(admin.ModelAdmin):
    list_display = ('farmer_name', 'phone', 'question', 'answer', 'submitted_at')
    search_fields = ('farmer_name', 'phone', 'question')
