from django.db import models


TagChoice = (
    ('Graphics', 'Graphics'),
    ('Web development', 'Web development'),
    ('UI/Ux', 'UI/Ux'),
)


class PortfolioTemplate(models.Model):
    name = models.CharField(max_length=20)
    portfolio_version = models.CharField(max_length=30)
    tag = models.CharField(max_length=20, choices=TagChoice)
    image = models.ImageField(upload_to='home_page/portfolio_tag')
    price = models.IntegerField(default=0)
    paid = models.BooleanField(default=True)

    @property
    def imageURL(self):
        try:
            image = self.image.url
        except:
            image = None
        return image

    def __str__(self):
        return f"{self.name} -- {self.paid}"
