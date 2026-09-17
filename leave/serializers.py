from rest_framework import serializers
from .models import LeaveRequest

class LeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest

        fields = ("__all__")

        read_only_fields = (
            "employee",
            "status",
            "created_at",
            "updated_at",
        )

        def validate(self, data):
            if data["end_date"] < data["start_date"]:
                raise serializers.ValidationError(
                    "End date cannot be before start date."
                )
            return data