from django.contrib import admin
from .models import LeaveRequest

# admin.site.register(LeaveRequest)

@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = (
        'employee',
        'leave_type',
        'status',
        'start_date',
        'end_date',
    )