from django.db import models


class DietLabel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Reference(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TriedCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Spice(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField()
    diet_labels = models.ManyToManyField(DietLabel)
    reference = models.ForeignKey(Reference, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tried_category = models.ForeignKey(TriedCategory, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)
    spices = models.ManyToManyField(Spice)
    comment = models.TextField()

    def __str__(self):
        return self.name
