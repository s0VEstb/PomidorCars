from django.db import models


class CarModel(models.Model):

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    mark = models.ForeignKey('MarkModel', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.name}"


class MarkModel(models.Model):

    class Meta:
        verbose_name = "Mark"
        verbose_name_plural = "Marks"

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name