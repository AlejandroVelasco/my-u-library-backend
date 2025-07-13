from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from books.views import BookViewSet
from checkouts.views import CheckoutViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

#adding viewsets to the router
router.register(r"users", UserViewSet, basename="user")
router.register(r"books", BookViewSet, basename="book")
router.register(r"checkouts", CheckoutViewSet, basename="checkout")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/login/", obtain_auth_token, name="api_token_auth"),
    path("api/", include(router.urls)),
]
