from django.db import models

class Membership(models.Model):
    title = models.CharField(max_length=500)  
    description = models.TextField()
    image = models.ImageField(upload_to='Membership/', blank=True, null=True)  

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Membership"
        verbose_name_plural = "Memberships"  # Corrected to plural form