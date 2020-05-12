import functools

import requests
from django.conf import settings
from django.http import HttpResponse

import responses
from user_management.models import RequestMock


def mockable(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not settings.DEBUG:
            return func(*args, **kwargs)
        with responses.RequestsMock() as rsps:
            for mock in RequestMock.objects.all():
                rsps.add(
                    method=mock.method,
                    url=mock.url,
                    body=mock.body,
                    status=mock.status,
                    content_type=mock.content_type,
                )
            return func(*args, **kwargs)

    return wrapper


@mockable
def api_call(request):
    content = requests.get("http://sennder.com")
    return HttpResponse(content)
