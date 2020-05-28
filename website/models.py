from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Tovar(models.Model):
    """Товары"""
    name = models.CharField("Имя товара", max_length=150)
    description = models.TextField("Описание")
    unit = models.CharField("Единица измерения", max_length=5)
    price = models.IntegerField("Цена", default=0)
    kol = models.IntegerField("Количество в магазине", default=0)
    date = models.DateField("Дата изготовления товара")
    img = models.ImageField("Изображение", upload_to="static/image")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Delivery(models.Model):
    """Доставка"""
    name = models.CharField("Наименование", max_length=150)
    kol = models.IntegerField("Количество товара для доставки", default=0)
    price = models.IntegerField("Цена", default=0)

    tovar = models.ForeignKey(Tovar, verbose_name="Товар", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Доставка"
        verbose_name_plural = "Доставки"


class Order(models.Model):
    """Покупка"""
    number = models.IntegerField("Номер накладной", default=0)
    date = models.DateField("Дата покупки")
    kol = models.IntegerField("Количество купленного")

    user = models.ForeignKey(User, verbose_name="Покупатель", on_delete=models.CASCADE)
    tovar = models.ForeignKey(Tovar, verbose_name="Товар", on_delete=models.CASCADE)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "Покупка"
        verbose_name_plural = "Покупки"