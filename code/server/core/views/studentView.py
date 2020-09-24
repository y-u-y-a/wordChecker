import json
from django.http import JsonResponse as Res
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from core.views.common import errorView
from core.models import Student
from core.serializers import StudentSerializer


def list(request):
    students = Student.objects.all()
    # [Object to Json]
    serial = StudentSerializer(instance=students, many=True)
    return Res(serial.data, safe=False)

@csrf_exempt
@require_POST
def find(request):
    try:
        # [Json to Dict]
        params = json.loads(request.body)
        first_name = params['first_name']
        student = Student.objects.get(first_name=first_name)
        # # [Object to Json]
        serial = StudentSerializer(instance=student)
        return Res(serial.data)
    except Exception as e:
        return errorView.my_error(e)
