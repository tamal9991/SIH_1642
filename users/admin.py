from django.contrib import admin
from .models import ContactUs,DomainForm,Feedback,Forum_details,Stack_details
# Register your models here.
admin.site.register(ContactUs)
admin.site.register(DomainForm)
admin.site.register(Feedback)
admin.site.register(Forum_details)
admin.site.register(Stack_details)