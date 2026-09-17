from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import LeaveRequest
from .serializers import LeaveRequestSerializer


class LeaveRequestListCreateView(generics.ListCreateAPIView):
    def get_queryset(self):
        return LeaveRequest.objects.filter(
            employee=self.request.user
        )
    serializer_class = LeaveRequestSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["status", "leave_type"]
    search_fields = [
        "reason",
    ]
    ordering_fields = [
        "start_date",
        "created_at",
    ]

    def perform_create(self, serializer):
        serializer.save(employee=self.request.user)



class LeaveRequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return LeaveRequest.objects.filter(
            employee=self.request.user
        )
    serializer_class = LeaveRequestSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["status", "leave_type"]
    search_fields = [
        "reason",
    ]
    ordering_fields = [
        "start_date",
        "created_at",
    ]