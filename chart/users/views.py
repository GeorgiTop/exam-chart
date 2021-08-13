from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from shapeshifter.views import MultiFormView


# class UserCreateView(SuccessMessageMixin, FormView):
#     form_class = UserRegisterForm
#     template_name = 'users/register.html'
#     success_message = 'Your account has been created!'
#     success_url = '../news'

class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('top20-home')

    def get_success_message(self, cleaned_data):
        self.success_message = f'Welcome {self.object}! Your account has been created!'
        return self.success_message % cleaned_data

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')
#             login(request, user)
#             messages.success(request, f'Welcome {username}! Your account has been created!')
#             return redirect('news-home')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/register.html', {'form': form})


# class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, MultiFormView):
#     form_classes = (UserUpdateForm, ProfileUpdateForm)
#     template_name = 'users/profile_cbv.html'
#     success_url = reverse_lazy('profile')
#     success_message = 'Your account has been updated!'


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
            return redirect('profile')
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




