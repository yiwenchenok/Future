from django.contrib import admin

# Register your models here.
from job.models import JobInfo

admin.site.site_header = '后台管理'
admin.site.site_title = '后台管理'
admin.site.index_title = '后台管理'


@admin.register(JobInfo)
class JobInfoAdmin(admin.ModelAdmin):
    list_display = ('coid', 'company_name', 'job_name')
