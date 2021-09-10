from datetime import datetime, timedelta

from django.conf import settings
from django.db import models
# Create your models here.
from django.db.models.signals import post_save
from paystackapi.paystack import Paystack
from paystackapi.transaction import Transaction
from dateutil.relativedelta import relativedelta

from membership.utils import datetime_from_reference
from users.models import User

from google_currency import convert
import requests

paystack_secret_key = settings.PAYSTACK_LIVE_KEY
paystack = Paystack(secret_key=paystack_secret_key)

# response = Customer.create(first_name='first_name', last_name='last_name', email='codertjay@gmail.com', phone='phone')
MembershipType = (
    ('Free', 'Free'),
    ('Standard', 'Standard'),
    ('Premium', 'Premium'),
    ('Professional', 'Professional'),
)


class CurrencyConverter():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        # first convert it into USD if it is not in USD.
        # because our base currency is USD
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]

        # limiting the precision to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 4)
        return amount


def convert_to_usd(amount):
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = CurrencyConverter(url)
    print(converter.convert("NGN", "USD", amount))
    currency = converter.convert("NGN", "USD", amount)
    return currency


class MembershipManager(models.Manager):
    def get_membership_type(self, membership_type):
        membership = self.filter(membership_type=membership_type)
        if membership:
            return membership.first()
        return None

    def get_membership_plan_id(self, membership_plan_id):
        membership = self.filter(membership_plan_id=membership_plan_id)
        if membership:
            return membership.first()
        return None


class Membership(models.Model):
    name = models.CharField(max_length=20)
    membership_type = models.CharField(
        choices=MembershipType, default='Free', max_length=50)
    membership_plan_id = models.CharField(max_length=40, blank=True, null=True)
    info = models.TextField()
    objects = MembershipManager()

    def __str__(self):
        return self.membership_type

    @property
    def interval(self):
        return paystack.plan.get(self.membership_plan_id)['data']['interval']

    @property
    def price(self):
        membership_price = 0
        try:
            print('paystack price', paystack.plan.get(
                self.membership_plan_id)['data']['amount'])
            membership_price = paystack.plan.get(self.membership_plan_id)[
                                   'data']['amount'] / 100
        except:
            membership_price = 0
        return membership_price

    @property
    def price_usd(self):
        price = convert_to_usd(self.discount)
        return price

    @property
    def discount(self):
        discount_price = 0
        try:
            print('paystack price', paystack.plan.get(
                self.membership_plan_id)['data']['amount'])
            discount_price = paystack.plan.get(self.membership_plan_id)[
                                 'data']['amount'] / 90
        except:
            discount_price = 0
        return discount_price

    @property
    def discount_usd(self):
        price = convert_to_usd(self.discount)
        return price


class UserMembershipSubscriptionManager(models.Manager):

    def get_user_subscription(self):
        pass


class UserMembershipSubscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    customer_code = models.CharField(max_length=100, blank=True, null=True)
    customer_id = models.CharField(max_length=100, blank=True, null=True)
    customer_reference = models.CharField(
        max_length=100, blank=True, null=True)
    objects = UserMembershipSubscriptionManager()

    def __str__(self):
        return f'{self.user.first_name} -- {self.user.last_name} -- {self.membership.membership_type}'

    @property
    def created_data(self):
        time = None
        try:
            reference = self.customer_reference
            response = Transaction.verify(reference=reference)
            time = datetime_from_reference(response)
        except:
            time = datetime.now()
        return time

    @property
    def expiration_date(self):
        paid_at = None
        try:
            reference = self.customer_reference
            response = Transaction.verify(reference=reference)
            paid_at = datetime_from_reference(response)
            interval = response['data']['plan_object']['interval']
            if interval == 'annually':
                expired_time = relativedelta(months=12)
            elif interval == 'quaterly':
                expired_time = relativedelta(months=6)
            elif interval == 'monthly':
                expired_time = relativedelta(months=1)
            paid_at += expired_time
        except:
            paid_at = datetime.now()
        return paid_at


def post_save_user_membership_subscription_create(sender, instance, created, *args, **kwargs):
    free_membership = Membership.objects.get_membership_type('Free')
    if free_membership:
        if created:
            UserMembershipSubscription.objects.get_or_create(user=instance,
                                                             membership=free_membership)
        user_membership, created = UserMembershipSubscription.objects.get_or_create(user=instance,
                                                                                    membership=free_membership)


post_save.connect(post_save_user_membership_subscription_create,
                  sender=settings.AUTH_USER_MODEL)
