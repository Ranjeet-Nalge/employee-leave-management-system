from django.db import models
from django.contrib.auth.models import User

class LeaveRequest(models.Model):

    employee = models.ForeignKey(
        User,on_delete=models.CASCADE,
        related_name='leave_request'
)

    Leave_Types = [
        ("Sick", "Sick"),
        ("Casual", "Casual"),
        ("Annual", "Annual"),
    ]

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
    ]

    leave_type = models.CharField(
        max_length=20,
        choices=Leave_Types,
    )

    start_date = models.DateField()

    end_date = models.DateField()

    reason = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee.username} - {self.reason} - {self.start_date} - {self.end_date} ."