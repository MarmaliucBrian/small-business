from django.db import models

# Create your models here.


class ServiciiModels(models.Model):
    name = models.CharField(max_length=300, null=False)
    description = models.CharField(max_length=300, null=False)

    def __str__(self):
        return f"{self.name} - {self.description}"