from rest_framework import serializers

from core.models import (
    Student
)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # use(only fields or exclude)
        fields = [
            'id',
            'email',
            'last_name',
            'first_name',
            'gender',
            'birthday',
            'phone_number',
            'ticket',
            'created_at',
            'updated_at',
            'is_staff',
            'is_active',
            'is_superuser'
        ]
