from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User must have an email!")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        if not password:
            raise ValueError("User must have a password!")
        user = self.create_user(email=email, password=password)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
