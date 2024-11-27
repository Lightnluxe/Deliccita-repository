from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """Категория пиццы (например, мясная, вегетарианская)."""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    """Модель пиццы."""
    name = models.CharField(max_length=200)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='pizzas')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='pizza_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    """Фотография пиццы (для галлереи)."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='pizza_images/')

    def __str__(self):
        return f"Фотография для {self.pizza.name}"


class Order(models.Model):
    """Заказ пиццы."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizzas = models.ManyToManyField(Pizza, through='OrderItem')
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) # Сумма заказа


class OrderItem(models.Model):
    """Элемент заказа (конкретная пицца в заказе)."""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2) # Цена за одну пиццу в этом заказе


class Profile(models.Model):
  """Профиль пользователя (дополнительная информация)."""
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  phone_number = models.CharField(max_length=20, blank=True)
  address = models.CharField(max_length=255, blank=True)

class Drink(models.Model):
    name = models.CharField(max_length=200)
    size = models.DecimalField(max_digits=6, decimal_places=2)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)


# Create your models here.
