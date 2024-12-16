from django.urls import path
from rest_framework.routers import DefaultRouter

from .viewsets import IndividualViewSet 


router = DefaultRouter()
router.register('individuals', IndividualViewSet)

urlpatterns = router.urls
