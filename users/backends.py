from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class CaseInsensitiveModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            case_insensitive_username_field = '{}__iexact'.format(UserModel.USERNAME_FIELD)
            user = UserModel._default_manager.get(**{case_insensitive_username_field: username})
        except UserModel.DoesNotExist:
            UserModel().set_password(password)  
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

class CustomEmailAuthenticationBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        email = kwargs['username'].lower()
        password = kwargs['password']
        try:
            user_with_email = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        else:
            if user_with_email.is_active and user_with_email.check_password(password):
                return user_with_email
        return None

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None