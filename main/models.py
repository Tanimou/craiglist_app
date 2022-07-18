from django.db import models

# Create your models here.
class Search(models.Model):
  search = models.CharField(max_length=500)
  created=models.DateTimeField( auto_now=True)#will set automatically the date time when an object is created

  #to specify a kind of representation we want to see in the admin page

  def __str__(self):
    return f"{self.search} {self.created}"
  class Meta:
      verbose_name_plural="Searches"