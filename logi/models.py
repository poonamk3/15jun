from django.db import models

# Create your models here.
class IndividualVideoDetail(models.Model):
	title = models.CharField(max_length=255,blank=False,null=False)
	description = models.TextField(max_length=1000,blank=False,null=False)
	created_at = models.DateTimeField(auto_now_add=True)
	



