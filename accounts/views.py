from django.shortcuts import render
from django.contrib.auth import get_user_model
# Create your views here.

def profile(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    context = {
        'user' : user,
    }
    return render(request, 'accounts/profile.html',context)