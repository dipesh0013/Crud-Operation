from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('Fullname','Mobile','Emp_code','position')
        labels = {
            'fullname':'Full Name'
        }
        def __init__(self,*args,**kwargs):
            super(EmployeeForm,self).__init__()
            self.fields['position'].empty_label="Select"
            #self.fields['Emp_code'].required= False