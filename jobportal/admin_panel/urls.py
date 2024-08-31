from django.urls import path
from .views import *
app_name='admin_panel'
urlpatterns = [
    
    path('',Dashboard.as_view(),name='dashboard'),
    path('dasboard/',Dashboard.as_view(),name='dashboard'),
    path('user-list/',UserListView.as_view(),name='user_list'),
    path('user/1',UserProfileView.as_view(),name='user_profile'),
    path('add-user/',AdduserView.as_view(),name='add_user'),
    path('list-company/',ListCompanyView.as_view(),name='list_company'),
    path('add-company/',AddCompanyView.as_view(),name='add_company'),
    path('company/1/',CompanyDetailView.as_view(),name='company_detail'),
    path('company-profile',CompanyProfileView.as_view(),name='company_profile'),
    path('list-job/',ListJobView.as_view(),name='list_job'),
    path('add-job/',AddJobView.as_view(),name='add_job'),
    path('profile/',AdminUserView.as_view(),name='admin_profile'),
    

    
]
