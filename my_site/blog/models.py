from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

#----------------------------------------------
#-------------------- POST --------------------
#----------------------------------------------
class Post(models.Models):
    title = models.CharField(max_length= 150)
    excerpt = models.CharField(max_length = 300)
    image_name = models.CharField(max_length = 100)
    created_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique = True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    