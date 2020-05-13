from django.db import models


#create a table in the database call Projects with the following column headings, this will be accesible in the admin page
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)


    def __str__(self):
        return self.title
