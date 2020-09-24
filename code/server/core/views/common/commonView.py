from django.http import JsonResponse as Res


def hello(request):
    return Res({
        'data': 'Hello World'
    })
