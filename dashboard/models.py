from django.db import models
from fontawesome_5.fields import IconField

from Portfolio.settings import DEFAULT_REDIRECT_URL
from users.models import User


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)
    description = models.CharField(max_length=200)

    @property
    def imageURL(self):
        try:
            image_ = self.image.url
            image = DEFAULT_REDIRECT_URL + image_
        except:
            image = ''
        return image

    def __str__(self):
        return f'{self.name} by{self.user.username}'


class ProjectItem(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    description = models.CharField(max_length=100)
    instagram = models.BooleanField(default=False)
    twitter = models.BooleanField(default=False)

    @property
    def imageURL(self):
        try:
            image_ = self.image.url
            image = DEFAULT_REDIRECT_URL + image_
        except:
            image = ''
        return image

    def __str__(self):
        return f'{self.name[0:10]} by - {self.user.username}'


class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    client_name = models.CharField(max_length=50)
    image = models.ImageField()
    url = models.URLField(blank=True, null=True)
    detail = models.CharField(max_length=200)

    @property
    def imageURL(self):
        try:
            image_ = self.image.url
            image = DEFAULT_REDIRECT_URL + image_
        except:
            image = ''
        return image


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    start_date = models.CharField(max_length=10)
    end_date = models.CharField(max_length=10)
    detail = models.CharField(max_length=200)


class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField()
    description = models.CharField(max_length=200)

    @property
    def imageURL(self):
        try:
            image_ = self.image.url
            image = DEFAULT_REDIRECT_URL + image_
        except:
            image = ''
        return image


skill_choices = (
    ('Meeting_and_Listening', 'Meeting & Listening'),
    ('UI/UX_Design', 'UI/UX Design'),
    ('PhotoShop', 'PhotoShop'),
    ('Branding_and_identity', 'Branding & identity'),
    ('Branding_and_identity', 'Branding & identity'),
    ('Technical_Support', 'Technical Support'),
)


class Skills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    percent = models.PositiveIntegerField(default=75)
    icon = IconField(blank=True, null=True)