from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from paystackapi.paystack import Paystack
from paystackapi.transaction import Transaction

from membership.models import Membership, UserMembershipSubscription

paystack_secret_key = settings.PAYSTACK_LIVE_KEY

paystack = Paystack(secret_key=paystack_secret_key)


@login_required()
def payment_view(request, payment_type=None):
    print(payment_type)
    membership = Membership.objects.get_membership_type(payment_type)
    user_membership = UserMembershipSubscription.objects.filter(user=request.user).first()
    if user_membership.membership.membership_type != 'Free':
        messages.success(request, 'Your current subscription is still active')
        return redirect('profile:dashboard')
    if membership:
        return render(request, 'HomePage/payment.html', {'membership_type': membership})
    else:
        messages.warning(request, 'Please click on the right link ')
        return redirect('home_page:price')


# 'T985946375823995'
@login_required()
def payment_done(request):
    print(request.POST)
    reference = request.POST.get('reference')
    if reference:
        response = Transaction.verify(reference=reference)
        if response['data']['status'] == 'success':
            print(response['data']['customer']['id'])

            customer_code = response['data']['customer']['customer_code']
            customer_id = response['data']['customer']['id']
            plan_code = response['data']['plan_object']['plan_code']
            membership_subscription = UserMembershipSubscription.objects.filter(user=request.user).first()
            membership = Membership.objects.get_membership_plan_id(plan_code)
            if membership_subscription and membership:
                membership_subscription.customer_code = customer_code
                if not membership_subscription.customer_id:
                    membership_subscription.customer_id = customer_id
                if not membership_subscription.customer_reference:
                    membership_subscription.customer_reference = reference
                membership_subscription.membership = membership
                membership_subscription.save()
                membership_name = response['data']['plan_object']['name']
                messages.success(request,
                                 f'Your payment was successful you now have access to {membership_name} plan ')
                return render(request, 'HomePage/payment_done.html')
    messages.error(request, 'There was an error performing your request ')
    return redirect('home_page:home')


"""    
# returns success if the payment was successful
print(response['data']['status'])

# the interval check
print(response['data']['plan_object']['interval'])
# the name of the plan
print(response['data']['plan_object']['name'])
# the plan code
print(response['data']['plan_object']['plan_code'])

# message returns verifiaction successful
print(response['message'])

# information about the customer 
print(response['data']['customer']['customer_code'])
print(response['data']['customer']['email'])
print(response['data']['customer']['id'])
"""
