from django.db import models
import uuid

# Create your models here.

class Customer(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	name = models.CharField(max_length=128)
	email = models.EmailField()
	password = models.CharField(max_length=20)
	created_at = models.DateField(auto_now=True)

	def __str__(self):
		return self.id

class Product(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	name = models.CharField(max_length=128)
	price = models.FloatField()
	img_url = models.CharField(max_length=128)
	created_at = models.DateField(auto_now=True)

	def __str__(self):
		return self.id

class CartItem(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
	qtd = models.IntegerField()
	total = models.FloatField()
	created_at = models.DateField(auto_now=True)

	def __str__(self):
		return self.id

class Cart(models.Model):
	customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
	cart_item_id = models.ForeignKey(CartItem, on_delete=models.CASCADE)
	total = models.FloatField()
