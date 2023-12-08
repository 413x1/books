from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    keywords = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
