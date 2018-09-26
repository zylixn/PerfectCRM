from django.contrib import admin
from crm import models

class CustomerAdmin(admin.ModelAdmin):
    # 显示
    list_display = ['name', 'source', 'contact_type', 'contact', 'consultant', 'consult_content', 'status', 'date']
    # 过滤
    list_filter = ['source', 'consultant', 'status', 'date']
    # 搜索，consultant是外键，必须加“__字段名”
    search_fields = ['contact', 'consultant__name']

admin.site.register(models.Role)
admin.site.register(models.CustomerInfo,CustomerAdmin)
admin.site.register(models.Student)
admin.site.register(models.CustomerFollowUp)
admin.site.register(models.Course)
admin.site.register(models.ClassList)
admin.site.register(models.CourseRecord)
admin.site.register(models.StudyRecord)
admin.site.register(models.Branch)
admin.site.register(models.Menus)
admin.site.register(models.UserProfile)
