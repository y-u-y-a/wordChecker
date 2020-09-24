from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)
from core.models import AbstractModel


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """通常のユーザー作成"""

        if not email:
            raise ValueError('Email must be .')

        user = self.model(
            email=self.normalize_email(email), # 大文字は小文字に変換
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password):
        """createsuperuserコマンドによるユーザー作成"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin, AbstractModel):
    class Meta:
        db_table = 'users'
        # abstract = True # creage table ?

    email = models.EmailField(verbose_name='メールアドレス', max_length=50, unique=True)
    is_active = models.BooleanField(verbose_name='ログイン権限', default=True)
    is_staff = models.BooleanField(verbose_name='管理者権限', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
