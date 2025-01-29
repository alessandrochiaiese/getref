from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import * 


class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User #get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control file-upload-info'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    #name_business = forms.CharField(widget=forms.TextInput(attrs={'required': False}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']


class UpdateBaseProfileForm(forms.ModelForm):
    
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=False,
        input_formats=['%Y-%m-%d']  # Formato ISO della data, come "YYYY-MM-DD"
    )
    city = forms.CharField(widget=forms.TextInput(attrs={'required': False, 'class': 'form-control'}))
    street = forms.CharField(widget=forms.TextInput(attrs={'required': False, 'class': 'form-control'}))
    CAP = forms.CharField(widget=forms.TextInput(attrs={'required': False, 'class': 'form-control'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'required': False, 'class': 'form-control'}))
    
    class Meta:
        model = Profile
        fields = ['birth_date', 'city', 'street', 'CAP', 'phone_number',]


class UpdateBusinessProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control file-upload-info'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    # business
    name_business = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})) 
    iva = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
     

    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'name_business', 'iva']


class EnterpriseForm(forms.ModelForm):
    class Meta:
        model = ProfileBusiness
        fields = [
            'number_job_request_desidered_per_week',
            'have_office_shop_to_receive_customers',
            'link_google_maps',
            'contact_number',
            'chamber_commerce_certificate',
            'insurance_policy_certificate',
            'region',
            'sectors',
            'holder',
            'company_name',
            'email',
        ]
        widgets = {
            'number_job_request_desidered_per_week': forms.NumberInput(attrs={'class': 'form-control'}),
            'have_office_shop_to_receive_customers': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'link_google_maps': forms.URLInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'chamber_commerce_certificate': forms.ClearableFileInput(attrs={'required': False, 'class': 'form-control'}),
            'insurance_policy_certificate': forms.ClearableFileInput(attrs={'required': False, 'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'sectors': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'holder': forms.TextInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['region'].queryset = Region.objects.all()
        self.fields['sectors'].queryset = Sector.objects.all()

