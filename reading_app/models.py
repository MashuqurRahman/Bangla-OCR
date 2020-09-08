from django.db import models

# Create your models here.
class ImageUpload(models.Model):
    lang_choice=(
        ('ben','Bangla'),
        ('eng','English'),
        ('ben+eng','Bangla & English')
    )
    image = models.ImageField(upload_to='images/')
    text =models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    language=models.CharField(max_length=20,choices=lang_choice,default='bangla')

    class Meta:
        ordering=('-created',)

   
