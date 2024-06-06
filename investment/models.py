from django.db import models

class Investment(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='investment/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Investment"
        verbose_name_plural = "Investments"