from django.db import models

# Create your models here.
class Pizza(models.Model):
    """ Class definition fo a Pizza"""
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Topping(models.Model):
    """ Class definition for a Topping """
    pizza = models.ForeignKey(Pizza, on_delete=models.DO_NOTHING)
    name = models.TextField()

    class Meta:
        verbose_name_plural = 'Toppings'

    def __str__(self):
        name = list(self.name)
        if len(name) > 50:
            return ''.join(name[:50]) + '...'
        return ''.join(name)