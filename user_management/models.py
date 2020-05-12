from django.db import models


class RequestMock(models.Model):
    name = models.TextField()
    request = models.TextField()
    response = models.TextField()

    def __str__(self):
        return self.name
