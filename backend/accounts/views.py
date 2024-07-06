from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from allauth.socialaccount.providers.naver.views import NaverOAuth2Adapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import user_email
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter

class NaverLogin(SocialLoginView):
    adapter_class = NaverOAuth2Adapter

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)
        if sociallogin.account.provider == 'kakao':
            data = sociallogin.account.extra_data
            user.email = data.get('kakao_account').get('email')
            user.first_name = data.get('properties').get('nickname')
            user.phone_number = data.get('kakao_account').get('phone_number')
            user.save()
        return user

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'username': user.username,
            'email': user.email,
            'phone_number': user.phone_number,
        })