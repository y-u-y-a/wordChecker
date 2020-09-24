import json
from django.test import TestCase

from core.models import Student
from core.views import studentView
from core.serializers import StudentSerializer


class StudentModelTest(TestCase):
    pass



class StudentViewTest(TestCase):
    def test_list(self):
        # 実関数の実行結果
        res = studentView.list('request') # bytes
        result = json.loads(res.content) # to list
        # 確認用データ
        students = Student.objects.all()
        serial = list(students)
        self.assertEqual(result, serial)
