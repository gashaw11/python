from django import forms
from datetime import datetime

class DateFormatter:
    pass
    # Your existing DateFormatter class here...

class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    date_of_birth = forms.CharField(max_length=20)
    
    def clean_date_of_birth(self):
        date_input = self.cleaned_data['date_of_birth']
        formatter = DateFormatter(date_input)
        formatted_date = formatter.format_date()
        
        if not formatted_date:
            raise forms.ValidationError("Invalid date format. Please enter a valid date.")
        return formatted_date
