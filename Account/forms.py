# -*- coding: utf-8 -*-

#  Copyright (c) 2021.  TheFox

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from Account.models import Giseo


class SignUpAccountForm(UserCreationForm):
    """Переделываем стандартную регистрацию из django, добавляя к ней поля ввода mail. Присваем ко всем полям class от bs"""
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}), max_length=100, label='Логин')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Эл. почтовый ящик'}), max_length=64, label='Эл. почтовый ящик')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}), max_length=50, label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}), max_length=50, label='Подтверждение пароля')

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)


class SignInAccountForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}), max_length=100, label='Логин пользователя')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}), max_length=50, label='Пароль')


class SignInGiseoForm(forms.ModelForm):
    login = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин', 'autocomplete': "new-password"}), max_length=150, label='Логин')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль', 'autocomplete': "new-password"}), max_length=100, label='Пароль')

    class Meta:
        model = Giseo
        fields = ('login', 'password', 'place', 'locality', 'type_of_oo', 'educational_organization')

    def __init__(self, *args, **kwargs):
        super(SignInGiseoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
