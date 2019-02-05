from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from users.forms import UserRegistrationForm
from users.models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.


def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        title = "Create an Account"
        form = UserRegistrationForm(
            request.POST or None,
            request.FILES or None
            )

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            new_user = authenticate(email=user.email, password=password)
            login(request, new_user)

            return redirect("home")

        context = {"title": title, "form": form}

        return render(request, "users/form.html", context)



def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('user_success'))
        else:
            context["error"] = "Provide valid credentials !!"
            return render(request, "users/login.html", context)
    else:
        return render(request, "users/login.html", context)

@login_required(login_url="/login/")
def success(request):
    context = {}
    context['user'] = request.user
    return render(request, "users/success.html", context)



def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))