from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=150,verbose_name='Titulo ')
    description = models.TextField() 
    link = models.URLField(max_length=180)
    image = models.ImageField(upload_to='projects',verbose_name='Imagen ')
    created = models.DateTimeField(auto_now_add=True )
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='proyecto'
        verbose_name_plural='proyectos'
        ordering=['-created']
    def __str__(self):
        return self.title
    

