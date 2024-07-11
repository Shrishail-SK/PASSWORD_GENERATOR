
from django.contrib import admin
from .models import AmazonPassword, FlipkartPassword, AWSPassword

admin.site.register(AmazonPassword)
admin.site.register(FlipkartPassword)
admin.site.register(AWSPassword)
