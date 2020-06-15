from django.contrib import admin
from .models import VCT,Prob_occur,Individual,Organization

# Register your models here.
class VCTAdminLook(admin.ModelAdmin):
    list_display =['pk', 'vct_name', 'vct_active_users', 'vct_developer']

admin.site.register(Prob_occur)
admin.site.register(Individual)
admin.site.register(Organization)
admin.site.register(VCT,VCTAdminLook)


