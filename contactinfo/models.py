from django.db import models

class ContactInfo(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number_one = models.CharField(max_length=15)  
    phone_number_two = models.CharField(max_length=15, blank=True, null=True)  
    address = models.CharField(max_length=255)
    facebook_link = models.URLField(max_length=500, blank=True, null=True)
    instagram_link = models.URLField(max_length=500, blank=True, null=True)
    linkedin_link = models.URLField(max_length=500, blank=True, null=True)
    youtube_link = models.URLField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"
        
        
class UserContact(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Get In Touch"
        verbose_name_plural = "Get In Touch"