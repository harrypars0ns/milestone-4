from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import ProfileForm


def profile(request):
    """ Show a user profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,

    }

    return render(request, template, context)