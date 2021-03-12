from django.conf import settings
from django.db import models

# Create your models here.
from django.db.models.signals import post_save

from users.models import User

MembershipType = (
    ('Free', 'Free'),
    ('Standard', 'Standard'),
    ('Premium', 'Premium'),
    ('Professional', 'Professional'),
)


class MembershipManager(models.Manager):
    def get_membership_type(self, membership_type):
        membership = self.filter(membership_type=membership_type)
        print('membership manager', membership)
        if membership:
            return membership.first()
        return None


class Membership(models.Model):
    name = models.CharField(max_length=20)
    membership_type = models.CharField(choices=MembershipType, default='Free', max_length=50)
    membership_plan_id = models.CharField(max_length=40)
    price = models.IntegerField()
    discount = models.IntegerField()
    info = models.TextField()
    objects = MembershipManager()

    def __str__(self):
        return self.membership_type


class UserMembershipSubscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.first_name} -- {self.user.last_name} -- {self.membership.membership_type}'


def post_save_user_membership_subscription_create(sender, instance, created, *args, **kwargs):
    free_membership = Membership.objects.get_membership_type('Free')
    if free_membership:
        print(free_membership)
        if created:
            UserMembershipSubscription.objects.get_or_create(user=instance,
                                                             membership=free_membership)
        user_membership, created = UserMembershipSubscription.objects.get_or_create(user=instance,
                                                                                    membership=free_membership)


post_save.connect(post_save_user_membership_subscription_create, sender=settings.AUTH_USER_MODEL)
