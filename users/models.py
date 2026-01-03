
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone
import uuid

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255, db_index=True)
    last_name = models.CharField(max_length=255, db_index=True)
    phone = models.CharField(max_length=255, db_index=True, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    profile_picture = models.CharField(max_length=255, default="https://res.cloudinary.com/dp3a4be7p/image/upload/v1686984832/user_eatapc.png")
    is_verified = models.BooleanField(default=False)
    account_number = models.CharField(max_length=255, db_index=True, null=True, blank=True)
    home_address = models.CharField(max_length=255, db_index=True, null=True, blank=True)
    country = models.CharField(max_length=255, db_index=True, null=True, blank=True)
    gender = models.CharField(max_length=255, db_index=True, null=True, blank=True)
    account_type = models.CharField(max_length=255, db_index=True, null=True, blank=True)
    account_type = models.CharField(max_length=255, db_index=True, null=True, blank=True)
    city = models.CharField(max_length=255, db_index=True, null=True, blank=True)
    zipcode = models.CharField(max_length=255, db_index=True, null=True, blank=True)
    balance = models.CharField(max_length=255, db_index=True,  default="0.00")
    is_banned = models.BooleanField(default=False)
    internal_revenew_required = models.BooleanField(default=False)
    is_limit = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    password = models.CharField(max_length=128)
    pin = models.CharField(max_length=4, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    objects = UserManager()

    def __str__(self):
        return self.email
