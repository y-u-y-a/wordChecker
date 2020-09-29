from django.db import models
from core.models import User

# (値, 表示名)
GENDER_CHOICES = (
    (0, '未回答'),
    (1, '男性'),
    (2, '女性'),
    (3, 'その他')
)
BOOL_CHOICES = (
    (0, False),
    (1, True)
)

class Teacher(User):
    class Meta:
        db_table = 'teachers'

    last_name = models.CharField(verbose_name='姓', max_length=30)
    first_name = models.CharField(verbose_name='名', max_length=30)
    phone_number = models.IntegerField(verbose_name='電話番号')
    gender = models.IntegerField(verbose_name='性別', choices=GENDER_CHOICES, default=0)
    birthday = models.DateField(verbose_name='誕生日')
    prefecture = models.CharField(verbose_name='都道府県', max_length=5)
    city = models.CharField(verbose_name='市区町村', max_length=100)
    address = models.CharField(verbose_name='番地以降', max_length=100)
    auth_flg = models.IntegerField(verbose_name='認証フラグ', choices=BOOL_CHOICES, default=0)

    def __str__(self):
        return self.first_name
