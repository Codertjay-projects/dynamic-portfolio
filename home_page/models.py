from django.db import models


# Create your models here.
class HomePageService(models.Model):
    name = models.CharField(max_length=20)
    info = models.CharField(max_length=70)
    image = models.ImageField(upload_to='home_page/service')

    @property
    def imageURL(self):
        try:
            image = self.image.url
        except:
            image = None
        return image

    def __str__(self):
        return self.name


class HomePageTestimonial(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='testimonial')
    description = models.CharField(max_length=50)

    @property
    def imageURL(self):
        try:
            image = self.image.url
        except:
            image = None
        return image

    def __str__(self):
        return self.name


class SubscribeUser(models.Model):
    email = models.EmailField()


    def __str__(self):
        return self.email
