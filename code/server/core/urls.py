from django.urls import path

from core.views import (
    studentView,
    lessonView
)

# [api/]
urlpatterns = [
    path('students/list/', studentView.list, name='students_list'),
    path('students/find/', studentView.find, name='student_find'),
]
