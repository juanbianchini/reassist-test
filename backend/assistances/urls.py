from django.urls import path
from rest_framework.routers import DefaultRouter

from .viewsets import AssistanceViewSet 


router = DefaultRouter()
router.register('assistances', AssistanceViewSet )

urlpatterns = router.urls