from django.db import models
from core.models import (
    AbstractModel,
    Teacher,
    Student
)

BOOL_CHOICES = (
    (0, False),
    (1, True)
)

# instance: Lesson Object, filename: reqeust.File
def get_upload_path(instance, filename):
    upload_path = f'lesson_image/{instance.pk}_{instance.title}.jpg'
    return upload_path


class Lesson(AbstractModel):
    class Meta:
        db_table = 'lessons'

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE) # 1対多
    applicants = models.ManyToManyField(Student, through='Application', related_name='applied_students') # 多対多
    liked_students = models.ManyToManyField(Student, through='Favorite', related_name='liked_students') # 多対多

    title = models.CharField(verbose_name='タイトル', max_length=100)
    detail = models.TextField(verbose_name='詳細')
    image = models.ImageField(verbose_name='イメージ画像', upload_to=get_upload_path, null=True, blank=True)
    application_limit = models.IntegerField(verbose_name='申込者数上限', default=0)
    required_ticket = models.IntegerField(verbose_name='必要チケット枚数', default=0)
    zoom_url = models.CharField( verbose_name='ZoomのURL', max_length=100)
    start_at = models.DateTimeField(verbose_name='開始日時')
    end_at = models.DateTimeField(verbose_name='終了日時')
    public_flg = models.IntegerField(verbose_name='公開フラグ', choices=BOOL_CHOICES, default=0)
    delete_flg = models.IntegerField(verbose_name='削除フラグ', choices=BOOL_CHOICES, default=0)

    def __str__(self):
        return self.title


class Application(AbstractModel):
    """ 申し込み情報 """
    class Meta:
        db_table = 'applications'
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

class Favorite(AbstractModel):
    """ お気に入り情報 """
    class Meta:
        db_table = 'favorites'
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
