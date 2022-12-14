from django.shortcuts import render


def allow_groups(groups=[], user=None):
    if groups is None:
        groups = []

    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            user_groups = user.groups.filtler(name__in=groups)

            if not user_groups:
                return render(request, '404.html')

            return view_func(request, *args, **kwargs)

        return wrapper

    if callable(groups):
        func = groups
        groups=[]
        return decorator(func)

    return decorator
