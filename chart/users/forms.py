from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'posts_per_page']

    # def save(self, commit=True):
    #     db_profile = Profile.objects.get(pk=self.instance.id)
    #     if commit:
    #         current_profile_image = str(db_profile.image)
    #         default_profile_image = 'default.png'
    #         image_path = join(settings.MEDIA_ROOT, current_profile_image)
    #         if current_profile_image != default_profile_image:
    #             os.remove(image_path)
    #     return super().save(commit)
