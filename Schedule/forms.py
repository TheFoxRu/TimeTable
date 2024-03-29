# -*- coding: utf-8 -*-

#  Copyright (c) 2021.  TheFox

from django import forms

from Schedule.models import Schedule

BOOL_CHOICES = ((True, 'Да'), (False, 'Нет'))


class CreateAffairScheduleForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Дата', 'type': 'date'}, format='%Y-%m-%d'),
                           label='Дата')
    affair = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Дело|Предмет'}), label='Дело|Предмет')
    time_start = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Начало дела', 'type': 'time'}),
                                 label='Начало дела')
    time_end = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Окончание дела', 'type': 'time'}),
                               label='Окончание дела')
    homework = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Домашнее задание'}), label='Домашнее задание', required=False)
    note = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заметка'}), label='Заметка', required=False)
    is_ready = forms.NullBooleanField(widget=forms.Select(attrs={'class': 'form-control'}, choices=BOOL_CHOICES), label='Готово?', required=True)

    class Meta:
        model = Schedule
        fields = ('date', 'affair', 'time_start', 'time_end', 'homework', 'note', 'is_ready')
