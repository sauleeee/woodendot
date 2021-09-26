from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(default='')
    img = models.CharField(max_length=200)
    category = models.CharField(default='',max_length=200)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'img': self.img,
            'category': self.category
        }

    def __str__(self):
        return f'{self.id}: {self.title}'


class ProductManager(models.Manager):
    def order_by_name(self,title):
        return self.order_by('title')


class Product(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(default='')
    price = models.CharField(default='',max_length=200)
    img = models.CharField(max_length=200)
    objects = ProductManager()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.id}: {self.title} | {self.price}'

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'price': self.price,
            'img': self.img,

        }


class Furniture(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(default='')
    price = models.CharField(default='',max_length=200)
    img = models.CharField(max_length=200)
    img2 = models.CharField(max_length=200)
    img3 = models.CharField(max_length=200)
    body2 = models.TextField(default='')
    img4 = models.CharField(max_length=200)
    body3 = models.TextField(default='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True,related_name='furniture')

    class Meta:
        verbose_name = 'Furniture'
        verbose_name_plural = 'Furnitures'

    def __str__(self):
        return f'{self.id}: {self.title} | {self.price}'

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'body':self.body,
            'price': self.price,
            'img': self.img,
            'img2': self.img2,
            'img3': self.img3,
            'body2': self.body2,
            'img4': self.img4,
            'body3': self.body3,
            'product': self.product.to_json()
    }


class Order(models.Model):
    img = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    price = models.CharField(default='',max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'{self.id}: {self.img} | {self.title} | {self.price} '

    def to_json(self):
        return {
            'id: ': self.id,
            'img': self.image,
            'title: ': self.name,
            'price': self.price
        }


class Review(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    text = models.TextField(default='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True,related_name='review')


    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f'{self.id}: {self.firstName} | {self.lastName} | {self.text}'

    def to_json(self):
        return {
            'id: ': self.id,
            'fistName': self.firstName,
            'lastName: ': self.lastName,
            'text': self.text,
        }
