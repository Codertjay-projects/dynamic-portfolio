from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.base import View
from membership.models import Membership


@login_required()
def payment_view(request, payment_type=None):
    print(payment_type)
    membership = Membership.objects.get_membership_type(payment_type)
    if membership:
        return render(request, 'HomePage/payment.html', {'membership_type': membership})
    else:
        messages.warning(request, 'Please click on the right link ')
        return redirect('home_page:price')


def payment_done(request):
    return redirect('home_page:home')
