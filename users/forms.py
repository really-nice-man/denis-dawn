from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=150, label="Имя пользователя")
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)
    relation_to_denis = forms.CharField(max_length=1, label="Отношение к Денису",
                                        widget=forms.Select(choices=Profile.RELATION_TO_DENIS_CHOICES))
    ready_to_register = forms.BooleanField(label="Обязуюсь хейтить Дениса до конца бытия",
                                           widget=forms.CheckboxInput)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'relation_to_denis', 'ready_to_register')