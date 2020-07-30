from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import availability

  
class AddAppointmentForm(forms.ModelForm):
    class Meta:
        model = availability
        fields = ('doctor','date','time')
        help_texts = {
                'date': ('Format: MM/DD/YY'),
        }

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=True)
    city = forms.CharField(max_length=200)
    address = forms.CharField(max_length=200)
    age = forms.IntegerField()
    gender_choice = [
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('O', 'OTHERS'),
    ]
    gender = forms.ChoiceField(choices = gender_choice, widget=forms.RadioSelect,label='Gender')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', )