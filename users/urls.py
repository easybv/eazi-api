from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    *router.urls,
    path('users/<uuid:pk>/update_balance/', UserViewSet.as_view({'patch': 'update_balance'}), name='user-update-balance'),
]