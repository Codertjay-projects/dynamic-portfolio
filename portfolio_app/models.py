from django.db import models
from users.models import User


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField()
    description = models.CharField(max_length=200)

    @property
    def imageURL(self):
        try:
            image = self.image.url
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
    tag = models.CharField(max_length=10)

    @property
    def imageURL(self):
        try:
            image = self.image.url
        except:
            image = ''
        return image

    def __str__(self):
        return f'{self.name[0:10]} by - {self.user.username}'
