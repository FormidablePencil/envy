from django.db import models

class AIFunctionality(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    code = models.TextField()

    def __str__(self):
        return self.name