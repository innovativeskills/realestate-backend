from django.db import models
from django.utils.translation import gettext_lazy as _


class AboutUs(models.Model):
    title_one = models.CharField(max_length=500, verbose_name=_("Title One"))
    title_two = models.CharField(max_length=500, verbose_name=_("Title Two"))
    description = models.TextField(verbose_name=_("Description"))
    image = models.ImageField(upload_to='about_us/', blank=True, null=True, verbose_name=_("Image"))
    video = models.FileField(upload_to='about_us/', max_length=100, blank=True, null=True, verbose_name=_("Video"))

    def __str__(self):
        return self.title_one

    class Meta:
        verbose_name = _("About Us")
        verbose_name_plural = _("About Us")

class TeamMember(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))
    image = models.ImageField(upload_to='teammember/', verbose_name=_("Image"))
    phone_number = models.CharField(max_length=15, verbose_name=_("Phone Number"))
    email = models.EmailField(verbose_name=_("Email"))
    facebook_link = models.URLField(max_length=500, blank=True, null=True, verbose_name=_("Facebook Link"))
    twitter_link = models.URLField(max_length=500, blank=True, null=True, verbose_name=_("Twitter Link"))
    instagram_link = models.URLField(max_length=500, blank=True, null=True, verbose_name=_("Instagram Link"))
    linkedin_link = models.URLField(max_length=500, blank=True, null=True, verbose_name=_("LinkedIn Link"))
    dribble_link = models.URLField(max_length=500, blank=True, null=True, verbose_name=_("Dribble Link"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Team Member")
        verbose_name_plural = _("Team Members")

