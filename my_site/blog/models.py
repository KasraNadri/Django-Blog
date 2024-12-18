from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

#----------------------------------------------
#-------------------- TAG ---------------------
#----------------------------------------------
class Tag(models.Model):
    caption = models.CharField(max_length = 20)

#----------------------------------------------
#------------------- AUTHOR -------------------
#----------------------------------------------
class Author(models.Model):
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length= 100)
    email_address = models.EmailField()

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
    author = models.ForeignKey(Author, on_delete = models.SET_NULL, related_name = 'posts')
    tags = models.ManyToManyRel(Tag)