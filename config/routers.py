from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, PatientViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('patients', PatientViewSet, basename='patients')
urlpatterns = router.urls