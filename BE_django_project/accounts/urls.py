from django.urls import path, include
from .views import RegisterView, LoginView, UserViewSet
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
     path("login/", LoginView.as_view(), name="login"),
     path("api/auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
     path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
     path('', include(router.urls)),
]
