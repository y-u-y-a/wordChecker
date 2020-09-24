from django.http import JsonResponse as Res


def my_error(e):
    return Res({
        'type': str(e.__class__.__name__),
        'message': str(e),
        'args': str(e.args)
    }, safe=False)
