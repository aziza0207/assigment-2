from rest_framework.permissions import IsAuthenticated


class IsDoctorPermission(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return request.user.role == "doctor"