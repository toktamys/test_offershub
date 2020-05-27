from django.contrib import admin

from asana_api.models import User, Project, Task


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    fields = ('name', 'email')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name',)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'executor')

    def add_view(self, request, form_url='', extra_context=None):
        self.exclude = ('asana_id',)
        return super(TaskAdmin, self).add_view(request)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.exclude = ('project', 'asana_id')
        return super(TaskAdmin, self).change_view(request, object_id)


admin.site.register(User, UserAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
