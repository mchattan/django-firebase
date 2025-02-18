from django import forms

class FCMTokenUpdateForm(forms.Form):
    previous_token = forms.CharField(
        max_length=2048,
        required=False,  # Allow empty values for first-time registration
        strip=True,
    )
    new_token = forms.CharField(
        max_length=2048,
        required=True,  # Must always have a new token
        strip=True,
    )
