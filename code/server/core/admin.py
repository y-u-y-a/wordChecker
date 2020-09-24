from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core.models import (
    Student,
    Teacher,
    Lesson,
)


class StudentAdmin(admin.ModelAdmin):
    """ 受講生 """
    # カラムリスト
    columns = [
        'id',
        'email',
        'password',
        'last_name',
        'first_name',
        'gender',
        'birthday',
        'phone_number',
        'ticket'
    ]
    # 並び順
    ordering = ['id']
    # 一覧ページ
    list_display = columns
    # 追加・変更ページ
    fieldsets = [
        ('認証情報', {'fields': ('email', 'password')}),
        ('権限', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('電話番号', {'fields': ('phone_number',)}),
        ('ユーザー情報', {'fields': ('last_name', 'first_name', 'gender', 'birthday')}),
        ('その他', {'fields': ('ticket',)}),
    ]


class TeacherAdmin(admin.ModelAdmin):
    """ 講師 """

    columns = [
        'id',
        'email',
        'password',
        'last_name',
        'first_name',
        'gender',
        'birthday',
        'phone_number',
        'prefecture',
        'city',
        'address',
        'auth_flg'
    ]

    ordering = ['id']
    list_display = columns
    fieldsets = [
        ('認証情報', {'fields': ('email', 'password')}),
        ('権限', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('電話番号', {'fields': ('phone_number',)}),
        ('ユーザー情報', {'fields': ('last_name', 'first_name', 'gender', 'birthday', 'prefecture', 'city', 'address', 'auth_flg')})
    ]





class LessonAdmin(admin.ModelAdmin):
    """ レッスン """

    columns = [
        'id',
        'teacher',
        'title',
        'image',
        'detail',
        'application_limit',
        'required_ticket',
        'zoom_url',
        'start_at',
        'end_at',
        'public_flg',
        'delete_flg'
    ]

    ordering = ['id']
    list_display = columns
    fieldsets = [
        ('レッスン情報', {'fields': (
            'teacher',
            'title',
            'image',
            'detail',
            'application_limit',
            'required_ticket',
            'zoom_url',
            'start_at',
            'end_at',
            'public_flg',
            'delete_flg'
        )}),
    ]


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Lesson, LessonAdmin)
