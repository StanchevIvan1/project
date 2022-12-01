from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from watch_shop.auth_app.models import Profile


class Product(models.Model):
    name = models.CharField(
        max_length=30
    )

    photo = models.ImageField(
        upload_to='products',
        default='blank_profile_image.jpeg',
    )

    description = models.TextField(
        max_length=300,
        validators=(MinLengthValidator(10),
                    ))

    price = models.DecimalField(max_digits=12,
                                decimal_places=6,
                                validators=(MinValueValidator(0),), )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.name

#
# class ShoppingCart(models.Model):
#     quantity = models.PositiveIntegerField(
#         validators=(MinValueValidator(0),)
#         , )
#
#     created_at = models.DateTimeField(
#         auto_now_add=True,
#     )
#
#     user = models.OneToOneField(
#         Profile,
#         primary_key=True,
#         on_delete=models.CASCADE,
#     )
#
#     product = models.ForeignKey(
#         Product,
#         primary_key=
#     )
#