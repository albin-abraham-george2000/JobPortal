from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.conf import settings
from ckeditor.fields import RichTextField

# Create your models here.


class Hobby(models.Model):
    hobby = models.CharField(max_length = 25)
    
    class Meta:
        verbose_name = 'Hobby'
        verbose_name_plural ='Hobbies'
    
    def __str__(self):
        return self.hobby
    
class Interest(models.Model):
    interest = models.CharField(max_length = 25)
    
    class Meta:
        verbose_name = 'Interest'
        verbose_name_plural ='Interests'

    def __str__(self):
        return self.interest
    

GENDER_CHOICES = (
        ('male','MALE'),
        ('female','FEMALE'),
        ('rather not say','RATHER NOT SAY')
    )
    
    
class CustomMyUser(AbstractUser):
    
    SMOKING_HABITS_CHOICES = (
        ('0','Never Smokers'),
        ('1','Light Smokers'),
        ('2','Moderate Smokers'),
        ('3','Heavy Smokers'),
    )
    
    DRINKING_HABITS_CHOICES = (
        ('0','Never Drinkers'),
        ('1','Light Drinkers'),
        ('2','Moderate Drinkers'),
        ('3','Heavy Drinkers'),
    )
    
    
    # COUNTRY_CODE = 
    
    
    COUNTRY_CHOICES = (
        ('india','INDIA'),
        ('america','AMERICA'),
        ('europe','EUROPE'),
        ('middle east','MIDDLE EAST'),
        ('canada','CANADA')
        
    )

    
    QUALIFICATION_CHOICES = (
        ("High School", "High School"),
        ("Associate's Degree", "Associate's Degree"),
        ("Bachelor's Degree", "Bachelor's Degree"),
        ("Master's Degree", "Master's Degree"),
        ("Doctorate", "Doctorate"),
        ("Professional Degree", "Professional Degree"),
        ("Certificate", "Certificate"),
        ("Diploma", "Diploma"),
        ("Postdoctoral", "Postdoctoral"),
        ("Vocational", "Vocational"),
        )
   
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=20, null=True, blank=True)
    mobile_number = models.CharField(max_length=15,null=True,blank=True)
    dob = models.DateField(null=True,blank=True)
    hobbies = models.ManyToManyField(Hobby)
    qualification = models.CharField(choices=QUALIFICATION_CHOICES,max_length = 100,null=True, blank=True)
    interest =models.ManyToManyField(Interest)
    profile_pic =models.ImageField(upload_to='users/profile_pics/',null=True, blank=True,default='user/profile_pics/Default_profile.png')
    short_reel = models.FileField(upload_to='users/short_reel/',blank=True,null=True,)
    smoking_habit = models.BooleanField(default=False)
    drinking_habit = models.BooleanField(default=False)
    address = models.CharField( max_length = 100,null = True, blank = True )
    city = models.CharField(max_length=100,null=True,blank=True)
    country = models.CharField(max_length=50,choices=COUNTRY_CHOICES)
    
    # save and delete the profile_pics and short_reel sections
    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = CustomMyUser.objects.get(pk=self.pk)
            if old_instance.profile_pic != self.profile_pic:
                old_instance.profile_pic.delete(save=False)
            if old_instance.short_reel != self.short_reel:
                old_instance.short_reel.delete(save=False)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.profile_pic.delete(save=False)
        self.short_reel.delete(save=False)
        super().delete(*args, **kwargs)  
        
    
    
    
    # gender = models.CharField( max_length= 15, choices = GENDER_CHOICES, null = True, blank = True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    @property
    def age(self):
        if self.dob:
            today = date.today()
            return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return None

class JobTitle(models.Model):
    title = models.CharField(max_length = 100, unique = True)
    
    def __str__(self):
        return self.title
class Skills(models.Model):
    skills = models.CharField(max_length = 100,unique = True)
    
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural ='Skills'
    
    def __str__(self):
        return self.skills
    
class Company(models.Model):
    name = models.CharField(max_length = 100)

    
    def __str__(self):
        return self.name

class JobProfile(models.Model):
    EXPERIENCE_LEVEL_CHOICE = {
    ('fresher','FRESHER'),
    ('expert','EXPERT'),
    
    }
    
    JOB_PROFILE_CHOICES = {
        ('jobseeker','JOB SEEKER'),
        ('employer','EMPLOYER'),
    }
    
    user = models.OneToOneField(CustomMyUser,on_delete=models.CASCADE,primary_key = True)
    title = models.ForeignKey(JobTitle, on_delete=models.CASCADE, null=True, blank=True)
    jobprofile = models.CharField(max_length=100, blank = True, null= True,choices=JOB_PROFILE_CHOICES)
    expertise = models.CharField(max_length = 100, blank= True,null = True ,choices=EXPERIENCE_LEVEL_CHOICE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length = 100,null=True, blank=True)
    
    def is_employer(self):
        return self.jobprofile == 'employer'
    
    def is_jobseeker(self):
        return self.jobprofile == 'jobseeker'
    
    def __str__(self):
        return self.user.full_name
    
class JobCategory(models.Model):
    category = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.category
    
class JobDescription(models.Model):
    JOB_TYPE_CHOICES = {
        
        ('full time','FULL TIME'),
        ('part time','PART TIME'),
        ('temporary','TEMPORARY'),
        ('contract','CONTRACT'),
    }
    
    user = models.ForeignKey(CustomMyUser, on_delete=models.CASCADE)
    job_title = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    job_category = models.ForeignKey(JobCategory,on_delete=models.CASCADE)
    company_name = models.ForeignKey(Company,on_delete = models.CASCADE)
    location = models.CharField(max_length = 100)
    salary_package = models.CharField(max_length = 100)
    vacancies = models.PositiveIntegerField() 
    job_type = models.CharField(max_length =100,choices = JOB_TYPE_CHOICES)
    experience = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 15,choices = GENDER_CHOICES)
    job_description = RichTextField()
    
    def __str__(self):
        return self.job_title.title
    
class Notification(models.Model):

    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length = 50)
    content = models.CharField(max_length = 150)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):  
        return self.subject
    
class JobApplication(models.Model):
    user = models.ForeignKey(CustomMyUser, on_delete=models.CASCADE)
    job = models.ForeignKey(JobDescription, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100,null = True,blank = True)
    designation = models.CharField(max_length=250,null = True, blank = True)
    last_working_date = models.DateField(null = True, blank = True)
    salary = models.PositiveIntegerField(null = True, blank = True)
    quit_reason = models.TextField(null = True, blank = True)

    def __str__(self):
        return f"{self.user} - {self.job}"
    
    
    
class NotificationList(models.Model):
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    user = models.ForeignKey(JobProfile, on_delete=models.CASCADE)
    read_status = models.BooleanField(default = False)
    
    def __str__(self):
        return self.notification.subject
    
 # ------------- Incomplete-------------
    # @property
    # def Topic_Group(self):
    #     id = self.notification_id
    #     topic = Notification.subject
    #     pass
    # # ------------- Incomplete-------------
    # @property 
    # def Topic_Group_Subscribers(self):
    #     id = self.notification_id
    #     topic_id = Notification
    #     user_id = CustomMyUser.objects.filter(notification_id=id)
    #     pass
    
    
    
    
    
    
    
    
    
    
    
    
    
    




    
    
    

    