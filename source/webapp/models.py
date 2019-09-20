from django.db import models

CATEGORY = (
    ('sport', 'Sport'),
    ('fruits', 'Fruits'),
    ('vegetables', 'Vegetables'),
    ('clothes', 'Clothes'),
    ('shoes', 'Shoes'),
)

class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='name')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='description')
    category = models.CharField(max_length=20, default='other', choices=CATEGORY)
    balance = models.PositiveIntegerField(verbose_name='balance')
    cost = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='cost')


def __str__(self):
    return self.name