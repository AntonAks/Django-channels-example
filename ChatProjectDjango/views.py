import logging
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SimpleLoginForm
from django.contrib.auth.models import User


logger = logging.getLogger(__name__)


def home_page(request):
    if request.method == 'POST':
        form = SimpleLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            logger.warning(f"username: {username}")
            user = User.objects.create_user(username, "", "password")
            user.save()

            authenticate(request, username=username)
            user = authenticate(request, username=username, password="password")
            if user is not None:
                login(request, user)

            logger.warning(f"user authenticated: {user}")

            return redirect('index')
    else:
        form = SimpleLoginForm()

    return render(request, 'home.html', {"form": form})
