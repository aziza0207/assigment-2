from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, PatientViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('patients', PatientViewSet, basename='patient')
urlpatterns = router.urls