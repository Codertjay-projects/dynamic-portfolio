from django.db import models

# Create your models here.
from Portfolio.settings import DEFAULT_REDIRECT_URL
from users.models import User


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
