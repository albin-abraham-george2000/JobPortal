from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import JobProfile,Notification,NotificationList,JobDescription

@receiver(post_save, sender=JobDescription)
def create_notification_list(sender, instance, created, **kwargs):
    if created:
        notification = Notification.objects.create(
        subject=f'New Job Posting:{instance.job_title.title}',
        content=f'A new job posting has been added: {instance.job_title.title}'
        )
        try:
            job_profiles = JobProfile.objects.filter(title=instance.job_title,jobprofile = 'jobseeker').exclude(user =  instance.user)
            for job_profile in job_profiles:
                NotificationList.objects.get_or_create(
                    user=job_profile,
                    notification=notification
                )
        except JobProfile.DoesNotExist:
            pass
            
        
        