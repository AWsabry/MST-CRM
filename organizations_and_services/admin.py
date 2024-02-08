from django.contrib import admin
from .models import Industry, Organizations, Projects, Project_Services,Documents
from import_export import resources
from import_export.admin import ImportExportModelAdmin



class OrganizationData(resources.ModelResource):
    class Meta:
        model = Organizations


class OrganizationAdmin(ImportExportModelAdmin):
    resources_classes = [OrganizationData]
    list_display = ('organization_name', 'organization_type', 'id')
    list_filter = ('organization_type','created',)
    search_fields = ('organization_name',)


class ProjectServicesAdminInline(admin.TabularInline):
    model = Project_Services


class ProjectDocumentsAdminInline(admin.TabularInline):
    model = Documents

class IndustryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created')
    search_fields = ('name',)


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('sales_name', 'project_name', 'description', 'total_project_cost', 'industry', 'organizations', 'quarter_closed', 'created')
    list_filter = ('industry', 'quarter_closed','sales_name',)
    raw_id_fields = ('organizations','industry',)
    autocomplete_fields = ['organizations','industry',]
    readonly_fields = ['total_project_cost',]
    search_fields = ['project_name','organizations',]
    inlines = [ProjectServicesAdminInline,ProjectDocumentsAdminInline,]

# class Project_ServicesAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'service_percentage_rate', 'project', 'single_service_cost', 'created')


 




# Register models with custom ModelAdmin classes
admin.site.register(Industry, IndustryAdmin)
admin.site.register(Organizations,OrganizationAdmin)
admin.site.register(Projects, ProjectsAdmin)
# admin.site.register(Project_Services, Project_ServicesAdmin)
