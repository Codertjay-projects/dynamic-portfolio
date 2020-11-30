from django.db import models
from django.urls import reverse

from Portfolio.settings import DEFAULT_REDIRECT_URL
from users.models import User
# Create your models here.
from django.conf import settings
from django.db.models.signals import post_save
from django_countries.fields import CountryField
from fontawesome_5.fields import IconField
from colorful.fields import RGBColorField

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
    icon = IconField(blank=True,null=True)


portfolio_choices = (
    ('portfolio_v1', 'portfolio_v1'),
    ('portfolio_v2', 'portfolio_v2'),
    ('portfolio_v3', 'portfolio_v3'),
    ('portfolio_v4', 'portfolio_v4')
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pics = models.ImageField(upload_to='profile_pics', default='profile_pics/profile_pics.jpg')
    logo = models.ImageField(blank=True, null=True)
    background_image = models.ImageField(upload_to='background_image',
                                         default='profile/backgroundImage.jpg')

    motto = models.CharField(blank=True, null=True, max_length=100)
    main_skill = models.CharField(blank=True, null=True, max_length=100)

    country = CountryField(multiple=False)
    address = models.CharField(max_length=200, blank=True, null=True)

    phone_number = models.IntegerField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    about = models.TextField(blank=True, null=True, max_length=1000)

    portfolio_version = models.CharField(max_length=20, choices=portfolio_choices, default='portfolio_v1')

    def get_portfolio_absolute_url(self):
        return reverse('portfolio:portfolio', kwargs={'username': self.user.username})

    def __str__(self):
        return f'{self.user.username} '

    @property
    def backgroundImageURL(self):
        try:
            image_ = self.background_image.url
            image = DEFAULT_REDIRECT_URL + image_
        except:
            image = ''
        return image

    @property
    def profilePicsImageURL(self):
        try:
            image_ = self.profile_pics.url
            image = DEFAULT_REDIRECT_URL + image_
        except:
            image = ''
        return image

    @property
    def logoImageURL(self):
        try:
            image_ = self.logo.url
            image = DEFAULT_REDIRECT_URL + image_
        except:
            image = ''
        return image


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    description = models.TextField()


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


background_colors = (
    ('dark', 'dark'),
    ('light', 'light')
)


class Layout(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    primary_color = RGBColorField(default='#FFFFFF')
    secondary_color = RGBColorField(default='#000000')
    background_color = models.CharField(choices=background_colors, max_length=10, default='light')


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


def post_save_user_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
        Layout.objects.get_or_create(user=instance)
    user_profile, created = Profile.objects.get_or_create(user=instance)
    user_layout, created = Layout.objects.get_or_create(user=instance)


post_save.connect(post_save_user_profile_create, sender=settings.AUTH_USER_MODEL)
