from django.db import models

class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


from .user import *
from .student import *
from .teacher import *
from .lesson import *


# 拡張Userの取り出し（サンプル）#####################################
# 1. 取得したemail, passwordでUser内で認証
# 2. 拡張Userモデル.get(user_ptr_id=User.pk)で検索して取得
# --------------------------------------------------------------
# >>> u = User.objects.get(email='~~~~')
# >>> u.id
# >>> 3
# >>> t = Teacher.objects.get(user_ptr_id=u.id)
# >>> t.first_name
# >>> 'yuya'

# about choices ##########################################
# Teacher.gender: 1, Teacher.get_gender_display: '男性'
##########################################################
