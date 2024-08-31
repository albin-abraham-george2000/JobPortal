from django.contrib.auth import login,logout,authenticate
from django.urls import reverse_lazy
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.mail import EmailMessage
from .forms import LoginForm,ForgotPasswordForm
from django.shortcuts import render,redirect,get_list_or_404
from django.contrib.auth.hashers import make_password
from django.views.generic import FormView, View,TemplateView,UpdateView,CreateView,DetailView,ListView
from django.template.loader import render_to_string
from .forms import SetNewPasswordForm,UserRegisterForm,RegisterNextStep,UserProtfolioForm,UserForm,UserExperienceForm,EmpolyerProfileForm,JobSeekerProfileForm,JobCreateForm,ApplicationForm
from .models import CustomMyUser,JobProfile,JobDescription,NotificationList,Skills,JobApplication
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import load_templates,generate_message


# ==========================USER LOGIN=======================================

class UserLoginView(View):
   template_name='core/users/login.html'
   form_class=LoginForm
   def get(self,request):
       form = self.form_class
       return render(request,self.template_name,{'form':form})
   
   @method_decorator(csrf_exempt)
   def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                # Use the generate_message function to get the success message
                success_message = generate_message('success_login', username=user.username)
                messages.success(request, success_message['message'])
                
                return redirect('core:home')
            else:
                if CustomMyUser.objects.filter(email=email).exists():
                    error_message = generate_message('incorrect_password')
                else:
                    error_message = generate_message('user_not_found')
                messages.error(request, error_message['message'])
                print(f"Error message: {error_message['message']}")
        else:
            # Handle form errors if needed
            messages.error(request, 'Please correct the errors below.')

        return render(request, self.template_name, {'form': form})
   
class UserLogoutView(View):
    def get(self,request):
        logout(request)
        messages.success(request,"Logged Out Successfully")
        return redirect('auth_users:login')
     

class UserRegisterView(FormView):
    form_class = UserRegisterForm
    template_name = 'core/users/register.html'
    success_url = reverse_lazy('auth_users:next-seg')
    
    def get(self,request,*args,**kwargs):
        return render (request,self.template_name,{'form':self.form_class}) 

        
    
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        
        if not form.is_valid():
            return render(request,self.template_name,{'form':form})
        
        
        user = form.save(commit= False)
        user.password = make_password(form.cleaned_data['password'])
        user.save()
        # First Time User login function
        user = authenticate(email= form.cleaned_data['email'],password= form.cleaned_data['password'] )
        if user is not None:
            login(request,user)
            return redirect(self.success_url)
        else:
            return redirect('auth_users:login')
        
# ==========================END=======================================


# ==========================PROFILE SECTION===========================
            
class ProfileView(TemplateView):
    model = CustomMyUser
    template_name = 'core/users/profile-view.html'
    context_object_name = 'user'
    # form_class = {
    #     'user_protfolio':UserProtfolioForm,
    #     'user_experience':UserExperienceForm,
    #     'user_hobby':CustomMyUser.hobbies,
    #     'user_interest':CustomMyUser.interest,
    # }
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       user = self.request.user
       skillslist = Skills.objects.all()
       context["hobbies"] = user.hobbies.all() 
       context["interests"] = user.interest.all() 
    #    context["address"] = get_list_or_404(,pk=self.request.user.pk)
       return context
   
    

class ProfileNextView(FormView):
    form_class =  RegisterNextStep
    template_name='core/users/next-seg.html'  
    success_url = reverse_lazy('auth_users:next-seg(employ)')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Profile updated successfully.')
        return super().form_valid(form)
        
# For modify the current details in the CustomMyUser User Model 
class UserUpdateView(UpdateView):

    model = CustomMyUser
    form_class = UserForm
    
    def get_object(self, queryset=None):
        return self.request.user
    
class Next_Segm_Employ(TemplateView):
    template_name='core/users/next-seg(employ).html'  
    
    
class EmpolyerProfile(CreateView):
    template_name = 'core/users/Empolyer/Empolyer_segm.html'
    model = JobProfile
    form_class = EmpolyerProfileForm
    success_url = reverse_lazy('auth_users:profile-view')
    
    
    def form_valid(self, form):
        profile = form.save(commit = False)
        profile.user = self.request.user
        profile.jobprofile = 'employer'
        profile.expertise = None
        profile.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})
    
class JobSeekerProfile(CreateView):
    template_name = 'core/users/job_seeker_segm.html'
    form_class = JobSeekerProfileForm
    model = JobProfile
    success_url = reverse_lazy('auth_users:profile-view')
    
    def form_valid(self, form):
        profile = form.save(commit = False)
        profile.user = self.request.user
        profile.jobprofile = 'jobseeker'
        profile.company = None
        profile.location = None
        profile.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})
    
# ==========================END=======================================

class EmpolyerJobPanelView(TemplateView):
    template_name = 'Job/empolyer/Job_panel.html'
    
class JobCandidateView(TemplateView):
    template_name = 'Job/candidate_request.html'
    
    
class JobDetailView(LoginRequiredMixin, DetailView):
    template_name = 'Job/job_detail.html'
    model = JobDescription
    context_object_name = 'job'
#                   
#    Implement a logging feature for debugging purposes
# 
#     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ApplicationForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = ApplicationForm(request.POST)
        user = request.user
        if form.is_valid():
            job_apply = form.save(commit= False)
            job_apply.user = user
            job_apply.job = self.get_object()
            job_apply.save()
            

            # Redirect to the job detail page after saving
            return redirect('auth_users:job_detail', pk=self.get_object().pk)
        else:
            # Render the same page with the form errors
            return self.get(request, *args, form=form)

    

class CreateJobView(LoginRequiredMixin,CreateView):
    form_class = JobCreateForm
    template_name = 'Job/create_job.html'
    # success_url = reverse_lazy('auth_users:job_detail' ,kwargs = {'pk',self.object.pk})
    def get_success_url(self):
      return reverse_lazy('auth_users:job_detail',kwargs = {'pk':self.object.pk})
  
    def form_valid(self,form):
        form.instance.user = self.request.user
        form.instance.company_name = self.request.user.jobprofile.company
        return super().form_valid(form)
    

# ==========================JOB NOTIFICATION SECTION========================
# @method_decorator(csrf_exempt, name='dispatch')
class MarkAsReadView(View):
    def get(self, request, *args, **kwargs):
        try:
            user = self.request.user.jobprofile
            notification = NotificationList.objects.filter(user=user,read_status = False)
            notification.update(read_status=True)
            return JsonResponse({'message': 'Notifications marked as read'}, status=200)
        
        except JobProfile.DoesNotExist:
            return JsonResponse({'error':'Profile not found'})
        

# ==========================JOB LISTING SECTION========================

class JobListView(ListView):
    
    template_name = 'Job/job_listing.html'
    model = JobDescription
    context_object_name = 'jobs_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context[""] = 
        return context
    
    

    
class AddBlockContent(View):
    template_name = 'core/users/add-block.html'
    
    
#========================= Notification System Section ==============================    




#=============================== END ===================================


    
#========================= Password Section ==============================

class ForgotPasswordView(FormView):
    template_name = 'core/users/forgot-password.html'
    form_class = ForgotPasswordForm
    success_url = reverse_lazy('auth_users:login')  

    def form_valid(self, form):
        email = form.cleaned_data['email']
        try:
            user = CustomMyUser.objects.get(email=email)
        except CustomMyUser.DoesNotExist:
            user = None

        if user is not None:
            try:
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                url = self.request.build_absolute_uri(reverse('auth_users:password_reset_confirm', kwargs={'uidb64': uid, 'token': token}))

                # Send email
                mail_subject = 'Password Reset Request'
                message = render_to_string('auth_users/password_reset_email.html', {
                    'user': user,
                    'url': url,
                })
                to_email = email
                send_email = EmailMessage(mail_subject, message, to=[to_email])
                send_email.content_subtype = 'html'
                send_email.send()

            except Exception as e:
                # Handle email sending failure
                messages.error(self.request, 'There was an error sending the password reset email. Please try again later.')
                return self.form_invalid(form)
        else:
            # Handle the case where the email does not exist in the database
            messages.error(self.request, 'No account found with this email address.')

        return super().form_valid(form)
    
    def form_invalid(self, form):
        # Optionally add custom behavior for invalid forms
        messages.error(self.request, 'There was an error with your submission. Please check the details and try again.')
        return super().form_invalid(form)
            
class PasswordResetConfirmView(FormView):
    template_name = 'auth_users/password_reset_confirm.html'
    form_class = SetNewPasswordForm
    success_url = reverse_lazy('auth_users:login')

    def form_valid(self, form):
        uidb64 = self.kwargs['uidb64']
        token = self.kwargs['token']
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = CustomMyUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomMyUser.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.set_password(form.cleaned_data['new_password1'])
            user.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
        
# ==========================END=======================================