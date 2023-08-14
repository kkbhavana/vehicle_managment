from django.contrib import admin

from .models import SuperAdmin, Admin, Customer, User

# Register your models here.
admin.site.register(User),
admin.site.register(SuperAdmin),
admin.site.register(Admin),
admin.site.register(Customer)
