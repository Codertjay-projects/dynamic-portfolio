from django.db import models

# Create your models here.
from fontawesome_5.fields import IconField

from users.models import User

skill_choices = (
    ('Meeting_and_Listening', 'Meeting & Listening'),
    ('UI/UX_Design', 'UI/UX Design'),
    ('PhotoShop', 'PhotoShop'),
    ('Branding_and_identity', 'Branding & identity'),
    ('Branding_and_identity', 'Branding & identity'),
    ('Technical_Support', 'Technical Support'),
)


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    percent = models.PositiveIntegerField(default=75)
    icon = IconField(blank=True, null=True)

