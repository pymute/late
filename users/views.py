from django.shortcuts import render
from .models import Profile


def profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'profile/profiles.html', {'profiles':profiles})
