from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    phone_number = forms.CharField(max_length=17, required=True)
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    address = forms.CharField(widget=forms.Textarea, required=True)
    id_document = forms.FileField(required=False, label="Pièce d'identité (optionnel pour test)")

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'date_of_birth', 'address', 'id_document', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Cet email est déjà utilisé.")
        return email

    def clean_date_of_birth(self):
        dob = self.cleaned_data.get('date_of_birth')
        from datetime import date
        age = (date.today() - dob).days // 365
        if age < 18:
            raise forms.ValidationError("Vous devez avoir au moins 18 ans.")
        return dob