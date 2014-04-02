# -*- coding: utf-8 -*-
from django import forms
from lib_app.models import Book

class Book_Edit_Form(forms.ModelForm):
    class Meta:
        model = Book   
        
