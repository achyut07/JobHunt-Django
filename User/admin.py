from django.contrib import admin

# Register your models here.
from User.models import User,Company,Jobsearch,Apply

class UserAdmin(admin.ModelAdmin):
	list_display = ('username','id','first_name','last_name','email','Department','Contactnum','Choose')
admin.site.register(User,UserAdmin)

class CompanyAdmin(admin.ModelAdmin):
	list_display = ('Companyname','Company_email','job_title','job_description','Location','Image','JobNature','Salary')
admin.site.register(Company,CompanyAdmin)

class JobsearchAdmin(admin.ModelAdmin):
	list_display = ('job_title',)
admin.site.register(Jobsearch,JobsearchAdmin)

class ApplyAdmin(admin.ModelAdmin):
	list_display=('Applier_email','Company_email','password','cv')
admin.site.register(Apply,ApplyAdmin)