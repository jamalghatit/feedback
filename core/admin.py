from django.contrib import admin

from .models import FeedbackModel

@admin.register(FeedbackModel)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['nome', 'OM', 'email', 'message', 'criado']
    readonly_fields = ['nome', 'OM', 'email', 'message', 'criado']
    
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    