from .models import NotificationList,CustomMyUser

    
def job_post(request):
    if request.user.is_authenticated:
        try:
            notifications = NotificationList.objects.filter(user = request.user.jobprofile).select_related('notification')
            return {'notifications': notifications}
        except:
            return {'notifications': None}  # or raise an exception here if you want to handle it gracefully
    else:
        return {}
    
def unread_notification_count(request):
    if request.user.is_authenticated:
        try:
            unread_notifications = NotificationList.objects.filter(user = request.user.jobprofile, read_status = False).count()
            return {'unread_notifications': unread_notifications}
        except:
            return {'unread_notifications': 0}  # or raise an exception here if you want to handle it gracefully
    else:
        return {}
        