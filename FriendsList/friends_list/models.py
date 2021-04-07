from django.db import models


class MyDB(models.Model):
    name = models.CharField('Ім`я', max_length=50)
    age = models.IntegerField('Вік')

    def __str__(self):
        result = f'Ім`я: {self.name}  -  {self.age}: років.'
        return result
