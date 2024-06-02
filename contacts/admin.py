from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

from contacts.models import Contact


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin, DynamicArrayMixin):
    pass


admin.site.site_header = 'Контакты СБИСа'
