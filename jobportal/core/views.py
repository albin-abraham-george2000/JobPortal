from django.views.generic import TemplateView,View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from auth_users.models import NotificationList,Company,JobTitle
from .forms import SearchForm



class HomeView(TemplateView):
    
    template_name = 'core/pages/home.html'
    
    
class AboutView(TemplateView):
    
    template_name = 'core/pages/about.html'
    
    
class ContactView(TemplateView):
    
    template_name = 'core/pages/contact.html'
    
class UserLoginView(TemplateView):

    template_name = 'core/users/register.html'


# =========Search Modal Options==========
class SearchView():
    def search(request):
        form = SearchForm(request.POST or None)
        job_search_instance = JobTitle.objects.all()
        company_search_instance = Company.objects.all()
        
        if form.is_valid():
            query = form.cleaned_data.get('query')
            if query :
                job_search_instance = job_search_instance.filter(title__iconatins=query)
                company_search_instance = company_search_instance.filter(name__icontains=query)

        context = {
            'form': form,
            'job_search_instance': job_search_instance,
            'company_search_instance': company_search_instance
        }
        return render(request, 'core/shared_component/search.html', context)
    

    
class ForgotPasswordView(TemplateView):
    
    template_name = 'core/users/forgot-password.html'

class ProfileView(TemplateView):
        
    template_name='core/users/profile-view.html'
    

    
class ChangePasswordView(TemplateView):
    template_name='core/users/change-password.html'
    

    

    
