from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Project(models.Model):
   project_name = models.CharField(max_length=100, unique=True)
   project_details = models.TextField()
   project_image = models.ImageField(upload_to='project_image', blank=True)
   project_url = models.URLField(blank=True)
   project_github_link = models.URLField(blank=True)
   slug = models.SlugField(blank=True)
   time_created = models.DateTimeField(auto_now_add=True, null=True)


   def __str__(self):
      return self.project_name

   def save(self, *args, **kwargs):
      self.slug = slugify(self.project_name)
      super().save(*args, **kwargs)