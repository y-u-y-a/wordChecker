from django.db import models
from core.models import User


GENDER_CHOICES = (
    (0, '未回答'),
    (1, '男性'),
    (2, '女性'),
    (3, 'その他')
)

class Student(User):

    class Meta:
        db_table = 'students'

    last_name = models.CharField(verbose_name='姓', max_length=30)
    first_name = models.CharField(verbose_name='名', max_length=30)
    gender = models.IntegerField(verbose_name='性別', choices=GENDER_CHOICES, default=0)
    birthday = models.DateField(verbose_name='誕生日', null=True, blank=True)
    phone_number = models.IntegerField(verbose_name='電話番号', null=True, blank=True)
    ticket = models.IntegerField(verbose_name='所持チケット', default=0)

    def __str__(self):
        return self.first_name
