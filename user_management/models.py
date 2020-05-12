from django.db import models


class RequestMock(models.Model):
    METHOD_CHOICES = (
        ("GET", "GET"),
        ("POST", "POST"),
        ("PUT", "PUT"),
        ("DELETE", "DELETE"),
    )
    CONTENT_TYPE_CHOICES = (
        ("application/json", "application/json"),
        ("text/plain", "text/plain"),
    )

    url = models.URLField()
    method = models.TextField(choices=METHOD_CHOICES)
    body = models.TextField()
    status = models.SmallIntegerField()
    content_type = models.TextField(choices=CONTENT_TYPE_CHOICES)

    def __str__(self):
        return f"{self.url} {self.method}"
