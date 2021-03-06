from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenObtainSlidingView,

    TokenRefreshSlidingView,
    TokenRefreshView,
)


from .views import CustomObtainTokenPairWithPhoneView, UserRegistrationPostView, UserRegistrationCreateViewSet, LogoutAndBlacklistRefreshTokenForUserView, LogoutAllView

urlpatterns = [
    path('token/obtain/pair/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # refresh & access token
    path('token/custom/obtain/pair/', CustomObtainTokenPairWithPhoneView.as_view(), name='token_custom_obtain_pair'),  # refresh & access token
    path('token/obtain/sliding/', TokenObtainSlidingView.as_view(), name='token_obtain_sliding'),  # token



    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/refresh/sliding/', TokenRefreshSlidingView.as_view(), name='token_refresh_sliding'),
    # Just Registration
    path('user/just/registration/', UserRegistrationPostView.as_view(), name="just_registration_user"),
    path('user/registration/redirect/', UserRegistrationCreateViewSet, name="registration_and_redirect_user"),
    path('blacklist/', LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='blacklist'),
    path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
]