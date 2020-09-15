from django.shortcuts import render

def profile(request):
    """ Show a user profile. """

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)