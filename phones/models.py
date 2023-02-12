from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    lte_exists = models.CharField(max_length=10)
    slug = models.SlugField(max_length=200)

