from django.urls import path,include
from .views import *
from django.views.generic import TemplateView

app_name = 'auth_users'

urlpatterns = [
    
    # -----------------------User Section ----------------------
    
    path('login/', UserLoginView.as_view(), name ='login'),
    path('logout/', UserLogoutView.as_view(), name ='logout'),
    path('register/', UserRegisterView.as_view(), name ='register'),
    path('forgot-password/', ForgotPasswordView.as_view(),name ='forgot_password'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name ='password_reset_confirm'),
   
    
    # ---------------------Profile View--------------------------
    
    path('profile-view/', ProfileView.as_view(), name ='profile-view'),
    path('next-segm/', ProfileNextView.as_view(), name ='next-seg'),
    path('add-block/',AddBlockContent.as_view(),name = 'add-block'),
    path('next-segm(Employ)/', Next_Segm_Employ.as_view(), name ='next-seg(employ)'),
    path('job-seeker-segm/', JobSeekerProfile.as_view(), name ='job-seeker-segm'),
    path('empolyer-seg/', EmpolyerProfile.as_view(), name ='empolyer-segm'),
    path('job-panel/', EmpolyerJobPanelView.as_view(), name ='empolyer-job-panel'),
    
    # ----------------------Job Section --------------------------
    path('create-job/',CreateJobView.as_view(), name = 'create_job'),
    path('candiate_list/',JobCandidateView.as_view(), name = 'candidate_request'),
    path('job/<int:pk>/',JobDetailView.as_view(), name = 'job_detail'),
    path('job-list/',JobListView.as_view(), name ='job_list'),
    
    
     # ----------------------Notification Section --------------------------

    path('mark_as_read/', MarkAsReadView.as_view(), name='mark_as_read'),
]
