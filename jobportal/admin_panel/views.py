from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Dashboard(TemplateView):
    template_name='admin_panel/dashboard.html'
class UserListView(TemplateView):
    template_name='admin_panel/user_list.html'
class AdduserView(TemplateView):
    template_name='admin_panel/add_user.html'
class UserProfileView(TemplateView):
    template_name='admin_panel/Sample/UserProfile.html'
class AddCompanyView(TemplateView):
    template_name='admin_panel/add_company.html'
class CompanyDetailView(TemplateView):
    template_name='admin_panel/company-detail.html'
class CompanyProfileView(TemplateView):
    template_name='admin_panel/company_profile.html'
class ListCompanyView(TemplateView):
    template_name='admin_panel/list_company.html'
class AddJobView(TemplateView):
    template_name='admin_panel/add_job.html'
class ListJobView(TemplateView):
    template_name='admin_panel/list_job.html'
class AdminUserView(TemplateView):
    template_name='admin_panel/superuser_profile.html'

