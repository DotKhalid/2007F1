from django.db import models

class Contact(models.Model):
	name =  models.CharField(max_length =50)
	email =  models.EmailField()
	subject =  models.CharField(max_length =50)
	message =  models.TextField()

	class Meta:
		db_table = "Contact"


# Create your models here.
