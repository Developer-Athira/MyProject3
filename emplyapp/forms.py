from django import forms
from .models import Emply

class DateInput(forms.DateInput):
    input_type ='date'

class EmplyForm(forms.ModelForm):
    class Meta:
        model=Emply
        fields=['name',
                'designation',
                
                'dateOfJ',
                'department',
                'salary',
                'email']
        labels={
            'name':'Name',
            'designation':'Designation',
           
            'dateOfJ':'DOJ',
            'department':'Department',
            'salary':'Salary',
            'email':'Email'
        }


        widgets={
            'date':DateInput()
        }


