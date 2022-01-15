from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
from django.forms import formset_factory
from .models import *
from . import models



class MathitisForm(forms.ModelForm):
    genethlia = forms.DateField(input_formats=['%d/%m/%Y'],
                                widget=DatePickerInput(format='%d/%m/%Y'))
    enarksi = forms.DateField(input_formats=['%d/%m/%Y'],
                              widget=DatePickerInput(format='%d/%m/%Y'))

    class Meta:
        model = InfoMathiti
        fields = ('onoma', 'epitheto', 'fotographia', 'diefthinsi',
                  'tk', 'perioxi', 'tilefonoS', 'genethlia', 'enarksi', 'kinito', 'group')

        widgets = {
            'onoma': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-transform: capitalize;'}),
            'epitheto': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-transform: capitalize;'}),
            'fotographia': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'diefthinsi': forms.TextInput(attrs={'class': 'form-control'}),
            'tk': forms.TextInput(attrs={'class': 'form-control'}),
            'perioxi': forms.TextInput(attrs={'class': 'form-control'}),
            'tilefonoS': forms.TextInput(attrs={'class': 'form-control'}),
            'kinito': forms.TextInput(attrs={'class': 'form-control'}),
        }


class GoniosForm(forms.ModelForm):
    class Meta:
        model = InfoGonios
        fields = ('gonios', 'onoma', 'epitheto', 'epankelma',
                  'tilefono', 'tilefonoE', 'email', 'allo')
        widgets = {
            'allo': forms.TextInput(attrs={'class': 'form-control'}),
            'onoma': forms.TextInput(attrs={'class': 'form-control', 'style': "text-transform: capitalize;"}),
            'epitheto': forms.TextInput(attrs={'class': 'form-control', 'style': "text-transform: capitalize;"}),
            'epankelma': forms.TextInput(attrs={'class': 'form-control'}),
            'tilefono': forms.TextInput(attrs={'class': 'form-control'}),
            'tilefonoE': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class ProvlimataForm(forms.ModelForm):

    class Meta:
        model = Provlimata
        fields = ('kardiaka', 'kardiakaLeptomeries', 'asthma', 'asthmaLeptomeries',
                  'lipothimia', 'lipothimiaLeptomeries', 'allo', 'alloLeptomeries')
        widgets = {
            'kardiaka': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'kardiakaLeptomeries': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'asthma': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'asthmaLeptomeries': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'lipothimia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'lipothimiaLeptomeries': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'allo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'alloLeptomeries': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }


class ProgressForm(forms.ModelForm):
    kup = forms.DateField(input_formats=['%d/%m/%Y'],
                          widget=DatePickerInput(format='%d/%m/%Y'))

    class Meta:
        model = ProgressMathiti
        fields = ('kup', 'epitixia', 'comment')
        
        widgets = {
            'epitixia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }

class ParalaviForm(forms.ModelForm):
    class Meta:
        model = InfoParalavi
        fields = ('sxesi', 'onoma', 'epitheto', 'tilefono')
        widgets = {
            'sxesi': forms.TextInput(attrs={'class': 'form-control'}),
            'onoma': forms.TextInput(attrs={'class': 'form-control', 'style': "text-transform: capitalize;"}),
            'epitheto': forms.TextInput(attrs={'class': 'form-control', 'style': "text-transform: capitalize;"}),
            'tilefono': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AdiesForm(forms.ModelForm):
    class Meta:
        model = Adies
        fields = ('fotografiaAdia', 'forma')
        widgets = {
            'fotografiaAdia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'forma': forms.FileInput(attrs={'class': 'custom-file-input'}),
        }


class GroupsForm(forms.ModelForm):

    class Meta:
        model = InfoGroups
        fields = ('arxi', 'telos','mera', 'group','groupNum')
        
        widgets = {
            'arxi': TimePickerInput(),
            'telos': TimePickerInput(),
        }


# Update Forms

class MathitisEditForm(forms.ModelForm):

    genethlia = forms.DateField(input_formats=['%d/%m/%Y'],
                                widget=DatePickerInput(format='%d/%m/%Y'))
    enarksi = forms.DateField(input_formats=['%d/%m/%Y'],
                              widget=DatePickerInput(format='%d/%m/%Y'))

    class Meta:
        model = InfoMathiti
        fields = ('onoma', 'epitheto', 'fotographia', 'diefthinsi',
                  'tk', 'perioxi', 'tilefonoS', 'kinito', 'group', 'genethlia','enarksi')

        widgets = {
            'onoma': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-transform: capitalize;'}),
            'epitheto': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-transform: capitalize;'}),
            'fotographia': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'diefthinsi': forms.TextInput(attrs={'class': 'form-control'}),
            'tk': forms.TextInput(attrs={'class': 'form-control'}),
            'perioxi': forms.TextInput(attrs={'class': 'form-control'}),
            'tilefonoS': forms.TextInput(attrs={'class': 'form-control'}),
            'kinito': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EnergoiForm(forms.ModelForm):
    class Meta:
        model = InfoMathiti
        fields = ('energos',)
        widgets = {
            'energos': forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': "margin:10px;"}),
        }

class ProvlimataEditForm(forms.ModelForm):

    class Meta:
        model = Provlimata
        fields = ('kardiaka', 'kardiakaLeptomeries', 'asthma', 'asthmaLeptomeries',
                  'lipothimia', 'lipothimiaLeptomeries', 'allo', 'alloLeptomeries')
        widgets = {
            'kardiaka': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'kardiakaLeptomeries': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'asthma': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'asthmaLeptomeries': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'lipothimia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'lipothimiaLeptomeries': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'allo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'alloLeptomeries': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }
    
class AdiesEditForm(forms.ModelForm):
    class Meta:
        model = Adies
        fields = ('fotografiaAdia', 'forma')
        widgets = {
            'fotografiaAdia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'forma': forms.FileInput(attrs={'class': 'custom-file-input'}),
        }

class GoniosEditForm(forms.ModelForm):
    class Meta:
        model = InfoGonios
        fields = ('gonios', 'onoma', 'epitheto', 'epankelma',
                  'tilefono', 'tilefonoE', 'email', 'allo')
        widgets = {
            'allo': forms.TextInput(attrs={'class': 'form-control'}),
            'onoma': forms.TextInput(attrs={'class': 'form-control', 'style': "text-transform: capitalize;"}),
            'epitheto': forms.TextInput(attrs={'class': 'form-control', 'style': "text-transform: capitalize;"}),
            'epankelma': forms.TextInput(attrs={'class': 'form-control'}),
            'tilefono': forms.TextInput(attrs={'class': 'form-control'}),
            'tilefonoE': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        
class ParalaviEditForm(forms.ModelForm):
    class Meta:
        model = InfoParalavi
        fields = ('sxesi', 'onoma', 'epitheto', 'tilefono')
        widgets = {
            'sxesi': forms.TextInput(attrs={'class': 'form-control'}),
            'onoma': forms.TextInput(attrs={'class': 'form-control', 'style': "text-transform: capitalize;"}),
            'epitheto': forms.TextInput(attrs={'class': 'form-control', 'style': "text-transform: capitalize;"}),
            'tilefono': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        
class ProgressEditForm(forms.ModelForm):
    kup = forms.DateField(input_formats=['%d/%m/%Y'],
                          widget=DatePickerInput(format='%d/%m/%Y'))

    class Meta:
        model = ProgressMathiti
        fields = ('kup', 'comment','epitixia')
        
        widgets = {
            'epitixia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }
        
        
class GroupsEditForm(forms.ModelForm):

    class Meta:
        model = InfoGroups
        fields = ('arxi', 'telos','mera')
        
        widgets = {
            'arxi': TimePickerInput(),
            'telos': TimePickerInput(),
        }
# Add Form

class GoniosAdd(forms.ModelForm):
    class Meta:
        model = InfoGonios
        fields = ('gonios', 'onoma', 'epitheto', 'epankelma',
                  'tilefono', 'tilefonoE', 'email', 'allo')
        widgets = {
            'allo': forms.TextInput(attrs={'class': 'form-control'}),
            'onoma': forms.TextInput(attrs={'class': 'form-control', 'style': "text-transform: capitalize;"}),
            'epitheto': forms.TextInput(attrs={'class': 'form-control', 'style': "text-transform: capitalize;"}),
            'epankelma': forms.TextInput(attrs={'class': 'form-control'}),
            'tilefono': forms.TextInput(attrs={'class': 'form-control'}),
            'tilefonoE': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class ParalaviAdd(forms.ModelForm):
    class Meta:
        model = InfoParalavi
        fields = ('sxesi', 'onoma', 'epitheto', 'tilefono')
        widgets = {
            'sxesi': forms.TextInput(attrs={'class': 'form-control'}),
            'onoma': forms.TextInput(attrs={'class': 'form-control', 'style': "text-transform: capitalize;"}),
            'epitheto': forms.TextInput(attrs={'class': 'form-control', 'style': "text-transform: capitalize;"}),
            'tilefono': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        
# parousiologio
class ParousiologioForm(forms.ModelForm):
    class Meta:
        model= Parousiologio
        fields=('parousia','mathitis')
        widgets={
            'parousia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

