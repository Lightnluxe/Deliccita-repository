from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """Категория пиццы (например, мясная, вегетарианская)."""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Instructions(models.Model):
    city = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)

    def __str__(self):
        return f"Этот ресторан находится в городе {self.city} по адрессу {self.adress}"

class Pizza(models.Model):
    """Модель пиццы."""
    name = models.CharField(max_length=200)
    weight = models.IntegerField(null=False)
    size = models.IntegerField(null=False)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='pizzas')
    price = models.IntegerField(null=False)
    image = models.ImageField(upload_to='pizza_images/', blank=True, null=True)

    class Meta:
        db_table = "pizzas"

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    """Ингридиент"""
    name = models.CharField(max_length=200)
    pizzas = models.ManyToManyField(Pizza, related_name="ingredients")

    def __str__(self):
        return self.name

# class Photo(models.Model):
#     """Фотография пиццы (для галлереи)."""
#     pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name='photos')
#     image = models.ImageField(upload_to='pizza_images/')
#
#     def __str__(self):
#         return f"Фотография для {self.pizza.name}"


class Order(models.Model):
    """Заказ пиццы."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField(null=False) # Сумма заказа
    pizzas = models.ManyToManyField(Pizza, through='OrderItem')

    def __str__(self):
            return "Ваш заказ готов"

class OrderItem(models.Model):
    """Элемент заказа (конкретная пицца в заказе)."""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, default=1)
    price = models.IntegerField(null=False) # Цена за одну пиццу в этом заказе


class Profile(models.Model):
    """Профиль пользователя (дополнительная информация)."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(null=False)
    address = models.CharField(max_length=255, blank=True)

class Basket(models.Model):
    name = models.CharField(max_length=200)
    pizzas = models.ManyToManyField(Pizza, related_name="pizzas_in_basket")

    def  __str__(self):
        return f"Вы отложили {self.pizzas} в корзину"

class Drink(models.Model):
    name = models.CharField(max_length=200)
    size = models.IntegerField(null=False)
    weight = models.IntegerField(null=False)
    price = models.IntegerField(null=False)

class News(models.Model):
    name = models.CharField(max_length=200)
    pizzas = models.ManyToManyField(Pizza, related_name="new_pizzas")

    def  __str__(self):
        return f"Новинки: {self.pizzas}"


pb1 = Basket("Mozzarella")
pb2 = Basket("Margaritta")
print(Basket)

# Create your models here.
