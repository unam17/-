from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, False)
        # Add any additional fields you want to save here
        user.phone_number = form.cleaned_data.get('phone_number')
        user.save()
        return user

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)
        # Add any additional fields you want to populate here
        user.phone_number = data.get('phone_number', '')
        return user