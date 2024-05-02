from django.db import models
from accounts.models import Role
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

class StudentApplication(models.Model):
    email=models.EmailField(max_length=50)
    parentEmail=models.EmailField(max_length=50, null=True)
    rollno=models.IntegerField(blank=True, null=True)
    phoneno=models.IntegerField(blank=True, null=True)
    fatherName=models.CharField(max_length=255, blank=True, null=True)
    branch=models.CharField(max_length=255, blank=True, null=True)
    semester=models.CharField(max_length=255, blank=True, null=True)
    hostelNumber=models.CharField(max_length=255, blank=True, null=True)
    roomNumber=models.IntegerField(blank=True, null=True)
    fromDate=models.DateField(blank=True, null=True)
    toDate=models.DateField(blank=True, null=True)
    reason = models.CharField(max_length=500, blank=True, null=True)
    parentContact=models.IntegerField(blank=True, null=True)

    # status choices
    PENDING = -1
    REJECTED = 0
    APPROVED = 1
    STATUS_CHOICES = (
        (PENDING, "Pending"),
        (REJECTED, 'Rejected'),
        (APPROVED, 'Approved'),
    )
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=PENDING)

    # parent response
    parent_responded =  models.SmallIntegerField(choices=STATUS_CHOICES, default=PENDING)
    
    # role
    role=models.ForeignKey(Role, related_name="student_applications", on_delete=models.CASCADE, null=True)

    # created at
    created_at = models.DateTimeField(auto_now_add=True, null=True)


@receiver(post_save, sender=StudentApplication)
def send_email(sender, instance, **kwargs):
    # send email 
    if instance.parent_responded == -1:
        html_message = render_to_string("student/parent_confirmation.html", {
            'application' : instance
        })
        plain_message = strip_tags(html_message)

        message = EmailMultiAlternatives(
            subject="Email from our Leave System",
            body=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            to=[instance.parentEmail],
        )

        message.attach_alternative(html_message, "text/html")
        message.send()
    elif instance.status == -1:
        html_message = render_to_string("leaveSystem/respond_request.html", {
            'application' : instance
        })
        plain_message = strip_tags(html_message)

        message = EmailMultiAlternatives(
            subject="Email from our Leave System",
            body=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            to=settings.STAFF_EMAIL_LIST,
        )

        message.attach_alternative(html_message, "text/html")
        message.send()
    
    html_message = render_to_string("student/student_update.html", {
        'application' : instance
    })
    plain_message = strip_tags(html_message)

    message = EmailMultiAlternatives(
        subject="Email from our Leave System",
        body=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        to=[instance.email],
    )

    message.attach_alternative(html_message, "text/html")
    message.send()
    
