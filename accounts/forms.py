from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Логин')
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput)


class CustomUserСreationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Подтвердите пароль', strip=False, required=True, widget=forms.PasswordInput)
    email = forms.EmailField(label='Email', required=True)

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'name',
            'email',
            'phone',
            'password',
            'password_confirm',
            )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Пароли не совпадают')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = (
            'name',
            'email',
            'phone',
            )
            