from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_viewset import (
    AppUserViewSet,
    RoleViewSet,
    UserRoleViewSet,
    NotificationViewSet,
    SystemAuditViewSet,
)

router = DefaultRouter()
router.register(r"users", AppUserViewSet)
router.register(r"roles", RoleViewSet)
router.register(r"user-roles", UserRoleViewSet)
router.register(r"notifications", NotificationViewSet)
router.register(r"system-audits", SystemAuditViewSet)

urlpatterns = [
    path("login/", AppUserViewSet.as_view({"post": "login"}), name="appuser-login"),
    path("", include(router.urls)),
]
