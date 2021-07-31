from django.db import models

# Create your models here.
from Portfolio.settings import DEFAULT_REDIRECT_URL
from users.models import User


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
