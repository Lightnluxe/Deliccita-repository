from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

# class Category(models.Model):
#     """Категория пиццы (например, мясная, вегетарианская)."""
#     name = models.CharField(max_length=100, unique=True)
#
#     def __str__(self):
#         return self.name
#
# class Instructions(models.Model):
#     city = models.CharField(max_length=100)
#     adress = models.CharField(max_length=100)
#
#     def __str__(self):
#         return f"Этот ресторан находится в городе {self.city} по адрессу {self.adress}"

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


# class Order(models.Model):
#     """Заказ пиццы."""
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     total_price = models.IntegerField(null=False) # Сумма заказа
#     pizzas = models.ManyToManyField(Pizza, through='OrderItem')
#     drinks = models.ManyToManyField(Pizza, through='OrderItem')
#
#     def __str__(self):
#             return "Ваш заказ готов"
#
# class OrderItem(models.Model):
#     """Элемент заказа (конкретная пицца в заказе)."""
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
#     quantity = models.IntegerField(null=False, default=1)
#     price = models.IntegerField(null=False) # Цена за одну пиццу в этом заказе
#
#
# class Profile(models.Model):
#     """Профиль пользователя (дополнительная информация)."""
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone_number = models.IntegerField(null=False)
#     address = models.CharField(max_length=255, blank=True)
#
# class Basket(models.Model):
#     name = models.CharField(max_length=200)
#     pizzas = models.ManyToManyField(Pizza, related_name="pizzas_in_basket")
#
#     def  __str__(self):
#         return f"Вы отложили {self.pizzas} в корзину"
#
# class Drink(models.Model):
#     name = models.CharField(max_length=200)
#     size = models.IntegerField(null=False)
#     weight = models.IntegerField(null=False)
#     price = models.IntegerField(null=False)
#
# class News(models.Model):
#     name = models.CharField(max_length=200)
#     pizzas = models.ManyToManyField(Pizza, related_name="new_pizzas")
#
#     def  __str__(self):
#         return f"Новинки: {self.pizzas}"
#

class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    phone = models.CharField(max_length=15, unique=True, blank=True, null=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True
    )


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.email