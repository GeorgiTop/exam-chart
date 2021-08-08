from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


# class UserCreateView(SuccessMessageMixin, FormView):
#     form_class = UserRegisterForm
#     template_name = 'users/register.html'
#     success_message = 'Your account has been created!'
#     success_url = '../news'


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            messages.success(request, f'Welcome {username}! Your account has been created!')
            return redirect('news-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('users/profile.html')
    else:
        u_form = UserUpdateForm(
            instance=request.user
        )
        p_form = ProfileUpdateForm(
            instance=request.user.profile
        )

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)




