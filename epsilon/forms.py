from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm,UsernameField
from django.utils.translation import gettext_lazy as _
User._meta.get_field('username').validators[1].limit_value = 15
from .models import Profile
class MyAuthForm(AuthenticationForm):
    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. "
        ),
        'inactive': _("This account is inactive."),
    }
    username = UsernameField(
        label='Username/Email',
        widget=forms.TextInput(attrs={'autofocus': True})
    )


class MyLoginView(LoginView):
    authentication_form = MyAuthForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {
            'username': "Required. 15 characters or fewer. Letters, digits and ./+/-/_ only. It's not case-sensitive.",
        }
    def clean(self):
        cleaned_data = super(UserRegisterForm, self).clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        if username and User.objects.filter(username__iexact=username).exists():
            self.add_error('username', 'A user with that username already exists.')
        elif '@' in username:
            self.add_error('username','Letters, digits and ./+/-/_ only')
        if email and User.objects.filter(email__iexact = email).first():
            self.add_error('email', 'You have already created an account with this Email Id')
        return cleaned_data
    def clean_username(self):
        data = self.cleaned_data['username']
        data= data.title()
        return data

class ProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['branch','year']