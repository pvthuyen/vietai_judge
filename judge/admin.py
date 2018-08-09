from django.contrib import admin
from .views import Assignment, Submission

class AssignmentAdmin(admin.ModelAdmin):
    model = Assignment

class SubmissionAdmin(admin.ModelAdmin):
    model = Submission

admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Submission, SubmissionAdmin)