from django.shortcuts import render


def page_not_found(request, exception):
    context = {"exception": exception,
               "status": 404,
               }
    return render(request, '404.html', context=context)


def handler_500(request, *args, **kwargs):
    context = {"status": 500,
               }
    response = render(request, '500.html', context=context)
    response.status_code = 400
    return response
