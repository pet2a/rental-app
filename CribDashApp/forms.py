from django import forms
from .models import ContactInquiry1, Appartment1

class ContactInquiryForm(forms.ModelForm):
    AGENT_CHOICES = [
        ('Agent A', 'Agent A'),
        ('Agent B', 'Agent B'),
        ('Agent C', 'Agent C'),
    ]

    agent_name = forms.MultipleChoiceField(
        choices=AGENT_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="Select Agents",
        required=True
    )

    class Meta:
        model = ContactInquiry1
        fields = ['name', 'email', 'phone', 'message', 'agent_name']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Your Phone Number (Optional)', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message', 'class': 'form-control', 'rows': 4}),
        }

class AppartmentForm(forms.ModelForm):
    class Meta:
        model = Appartment1
        fields = ['name', 'price', 'description', 'image', 'location', 'bedrooms']

