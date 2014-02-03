from django.contrib import admin
from pollapp.models import Poll,Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class PollAdmin(admin.ModelAdmin):
   
    inlines = [ChoiceInline]
    exclude = ('ip_address','fingerprint',)

admin.site.register(Poll,PollAdmin)

