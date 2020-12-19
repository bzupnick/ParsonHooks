from django.contrib import admin
from src.models import User, Webhook, Message, Script, Secret

# Register your models here.
admin.site.register(User)
admin.site.register(Webhook)
admin.site.register(Message)
admin.site.register(Script)
admin.site.register(Secret)
