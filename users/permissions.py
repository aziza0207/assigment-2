from rest_framework.permissions import IsAuthenticated


class IsDoctorPermission(IsAuthenticated):
    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated
            and getattr(request.user, "role", None) == "doctor"
        )
