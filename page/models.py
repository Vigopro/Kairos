from django.db import models

class Category(models.Model):
	name = models.CharField('Название категории', max_length = 30, unique = True)
	description = models.TextField('Описание')

	class Meta:
		verbose_name = "категория"
		verbose_name_plural = "категории"
	
	def __str__(self):	
		return self.name		

class Good(models.Model):
	name = models.CharField('Наименование товара', max_length = 50, unique = True)
	description = models.TextField('Описание')
	in_stock = models.BooleanField(default = True, db_index = True)
	category = models.ForeignKey(Category, null = True, blank = True, on_delete = models.SET_NULL)
	price = models.PositiveIntegerField(null = False, blank = False)

	def __str__(self):
		s = self.name
		if not self.in_stock:
			s = s + " (нет в наличии)"
		return s

	class Meta:
		ordering = ["-price", "name"]
		unique_together = ("category", "name", "price")
		verbose_name = "товар"
		verbose_name_plural = "товары"