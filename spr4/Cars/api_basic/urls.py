from django.urls import path, include
from .views import GenericAPIView, CarViewSet, CarAPIView, CarDetails
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('car', CarViewSet, basename='car')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:id>/', include(router.urls)),
    path('car/', CarAPIView.as_view()),
    path('detail/<int:id>/', CarDetails.as_view()),
    path('generic/car/<int:id>/', GenericAPIView.as_view()),
]


