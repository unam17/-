# accounts/urls.py
from django.urls import path
from .views import GoogleLogin, KakaoLogin, NaverLogin, UserProfileView

urlpatterns = [
    path('google/login/', GoogleLogin.as_view(), name='google_login'),
    path('kakao/login/', KakaoLogin.as_view(), name='kakao_login'),
    path('naver/login/', NaverLogin.as_view(), name='naver_login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
