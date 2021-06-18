from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    """
    用户表，新增字段如下
    """
    GENDER_CHOICES = (
        ("1", "男"),
        ("0", "女")
    )

    gender = models.IntegerField(choices=GENDER_CHOICES, default="0", verbose_name="性别")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
