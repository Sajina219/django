from django import forms
from .models import AppleDevice, AppleVersion

# Form for AppleDevice
class AppleDeviceForm(forms.ModelForm):
    class Meta:
        model = AppleDevice
        fields = ['name', 'release_date']  # specify fields to show
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'})
        }

# Form for AppleVersion
class AppleVersionForm(forms.ModelForm):
    class Meta:
        model = AppleVersion
        fields = ['device', 'version_name', 'version_number', 'release_date']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'})
        }
