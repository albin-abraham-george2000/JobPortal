from django import forms
from .validator import validate_video_file
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import CustomMyUser,JobProfile,JobDescription,Skills,JobApplication


class UserRegisterForm(forms.ModelForm):
    
    username = forms.CharField(
        label = 'username' ,
        max_length = 23,
         required= True,
        widget = forms.TextInput (
            attrs = {
                'class':'form-control',
                
        }))
    
    full_name = forms.CharField( 
        label = 'Full Name' ,
         required= True,
        max_length = 23,
        widget = forms.TextInput (
            attrs = {
                'class':'form-control',
                
        }))
    
    email = forms.EmailField (
        label = 'Email',
        validators = [validate_email],
        error_messages = {
            'required':'Please enter a valid email address.',
            
        },
        widget = forms.TextInput(
            attrs= {
                'class':'form-control',
            }
            
    ))
    def Validate_mobile_number(value):
        if not value.isdigits():
            raise ValidationError('Mobile number must contain only digits.')
        if len(value) != 10:
            raise ValidationError('Mobile number must be 10 digits.')
    
    mobile_number = forms.CharField(
        label = 'Mobile No.',
        required= True,
        max_length = 10 ,
        validators =[Validate_mobile_number],
        error_messages ={
            'required':'Please enter a valid mobile number.'
        },
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                
            }
        ))
    
    password= forms.CharField(
        label = 'Password',
        max_length =  17, 
         min_length=5,
        required=True,
        error_messages = {
            'required':'Please enter password greater than 4 character.',
            'min_length':'Password must be at least 5 characters long.',
        },
        widget = forms.PasswordInput(
            attrs= {
                'class':'form-control',
            }
        ))
    
    password2= forms.CharField(
        label = 'Confirm Password' ,
        widget = forms.PasswordInput(
            attrs= {
                'class':'form-control',
            }
        ))
    
    
    class Meta:
        model = CustomMyUser
        fields = ['full_name','email','mobile_number','password','username']
        
        def clean_mobile_number(self):
            mobile_number = self.cleaned_data.get('mobile_number')
            if not mobile_number.isdigit():
                raise ValidationError('Mobile number must contain only digits.')
            if len(mobile_number) != 10:
                raise ValidationError('Mobile number must be 10 digits long.')
            return mobile_number
        
        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get("password")
            password2 = cleaned_data.get("password2")

            if password and password2 and password != password2:
                self.add_error('password2', "Passwords do not match. Please enter the same password in both fields.")

            return cleaned_data



class RegisterNextStep(forms.ModelForm):
    SMOKING_HABIT_CHOICES = {
        ('0','Never Smokers'),
        ('1','Light Smokers'),
        ('2','Moderate Smokers'),
        ('3','Heavy Smokers'),   
    }
    DRINKING_HABIT_CHOICES = {
        ('0','Never Drinkers'),
        ('1','Light Drinkers'),
        ('2','Moderate Drinkers'),
        ('3','Heavy Drinkers'),
    }
    
    class Meta:
        model = CustomMyUser
        fields = ['dob','hobbies','qualification','interest','profile_pic','short_reel','smoking_habit','drinking_habit']
        widgets = {
            'dob': forms.DateInput({ 
              'class':'form-control',
              'type':'date'
              
              
            }),
            'hobbies':forms.SelectMultiple({
                'class': 'form-control'
            }),
            'interest':forms.SelectMultiple({
                'class': 'form-control'
            }),
            'qualification':forms.Select({
                'class': 'form-control'
            }),
            'smoking_habit':forms.CheckboxInput({
                
            }),
            'drinking_habit':forms.CheckboxInput({
                
            }),
            'profile_pic':forms.FileInput({
                'class': 'form-control'
            }),
            'short_reel':forms.FileInput({
                'class': 'form-control'
            }),
        }
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        for field_name, field_instance in self.fields.items():
            field_instance.required = True
   
    def clean_short_reel(self):
        short_reel = self.cleaned_data.get('short_reel', False)
        if not short_reel:
            raise forms.ValidationError("No file chosen!")

        validate_video_file(short_reel)
        return short_reel
    
class UserForm(forms.ModelForm):
    class Meta:
        model = CustomMyUser
        fields = ['full_name', 'email', 'mobile_number', 'dob', 'qualification', 'profile_pic', 'short_reel', 'smoking_habit', 'drinking_habit']
    

class UserExperienceForm(forms.ModelForm):

    cv_upload = forms.FileField(
     widget = forms.FileField()   
    )
    
class UserProtfolioForm(forms.Form):
    
    
    project_name = forms.CharField(
        max_length = 100,
        label = 'Project Name',
        widget = forms.TextInput(
            attrs= {
                'class':'form-control',
                'placeholder':'Enter the project Name'
            }    
        ))
    
    project_description = forms.CharField(
        max_length = 100,
        label = 'Project Description',
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Enter the project Description'
            }    
        ))
    project_start_date = forms.DateField(

        label = 'Start Date',
        widget = forms.DateInput(
            attrs= {
                'class':'form-control'
            }
        ))
    
    project_end_date = forms.DateField(

        label = 'End Date',
        widget = forms.DateInput(
            attrs= {
                'class':'form-control'
            }
        ))
    
    project_links = forms.URLField()
    
    project_skill = forms.CharField(
        max_length = 100,
        label = 'Used Technologies',
        widget = forms.TextInput(
            attrs = {
                'class':'form-control'
            }
        )
    )

    
class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length = 255,required= True,
        label='Email',widget = forms.EmailInput(
        attrs ={
            
            'class':'form-control',
            'autofous':True,
        }))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(
        attrs = {
            
            'class':'form-control'
        }
    ))
    
    
class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        max_length = 255,required= True,
        label='Email',widget = forms.EmailInput(
        attrs ={
            'placeholder':'Enter the your email address'
        }))
    
class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=254)

    def clean_email(self):
        email = self.cleaned_data['email']
        if not CustomMyUser.objects.filter(email=email).exists():
            raise forms.ValidationError("No user is associated with this email address")
        return email

class SetNewPasswordForm(forms.Form):
    new_password1 = forms.CharField(label="New Password", widget=forms.PasswordInput)
    new_password2 = forms.CharField(label="Confirm New Password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("new_password1")
        password2 = cleaned_data.get("new_password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data
    
    
class SkillsChoiceForm(forms.ModelForm):
    model = Skills
    widgets = {
        'skills': forms.SelectMultiple(
            attrs =
            {
                'class':'form-control',
                'placeholder':'Select your skills',
            })
    }
    
class EmpolyerProfileForm(forms.ModelForm):
    
    class Meta:
        model = JobProfile
        fields = ['title','company','location']
        widgets = {
            'title': forms.Select(
                attrs = {
                    'class':'form-control',
                    'required':True
                }),
            
            'company': forms.Select(
                attrs={
                    'class':'form-control',
                    'required':True
                }),
            'location': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'required':True
                }
            )
            }
    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     instance.job_profile = 'employer'
    #     instance.expertise = None
    #     if commit:
    #         instance.save()
    #     return instance

class JobCreateForm(forms.ModelForm):
    
    class Meta:
        model = JobDescription
    
        exclude = ['user', 'company_name']
        
        widgets = {
            'job_title': forms.Select(
                attrs= {
                    'class':'form-control',
                }
            ),
            
            'job_category': forms.Select(
                attrs= {
                    'class':'form-control',
                }
            ),
            
            'location': forms.TextInput(
                attrs= {
                    'class':'form-control',
                }
            ),
            'salary_package': forms.TextInput(
                attrs= {
                    'class':'form-control',
                }
            ),
            
            'vacancies': forms.NumberInput(
                attrs= {
                    'class':'form-control',
                }
            ),
            
            'job_type': forms.Select(
                attrs= {
                    'class':'form-control',
                }
            ),
            
            'experience': forms.TextInput(
                attrs= {
                    'class':'form-control',
                }
            ),
            
            'gender': forms.Select(
                attrs= {
                    'class':'form-control',
                }
            ),
            
        }
   
class ApplicationForm(forms.ModelForm):
    
    class Meta:
        model = JobApplication
        fields = ['company_name', 'designation', 'last_working_date', 'salary', 'quit_reason']
        
        widgets = {
            'last_working_date': forms.DateInput(
                attrs ={
                    'type':'date'
                })
        }

class JobSeekerProfileForm(forms.ModelForm):
    
    class Meta:
        model = JobProfile
        fields = ['title','expertise']
        widgets = {
            'title': forms.Select(
                attrs = {
                    'class':'form-control',
                    'required':True
                }),
            
            'expertise': forms.Select(
                attrs={
                    'class':'form-control',
                    'required':True
                }),
        
            }
    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     instance.job_profile = 'jobseeker'
    #     instance.company = None
    #     instance.location = None
    #     if commit:
    #         instance.save()
    #     return instance

   