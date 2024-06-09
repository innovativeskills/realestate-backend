from django.db import models
from teammember.models import TeamMember
from ckeditor.fields import RichTextField


class Project(models.Model):
    project_name = models.CharField(max_length=500)
    project_code = models.CharField(max_length=100)
    description = RichTextField()
    brochure_pdf = models.FileField(upload_to='brochures/', max_length=100)
    agent = models.ForeignKey(TeamMember, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = "Company Summary"
        verbose_name_plural = "Company Summaries"