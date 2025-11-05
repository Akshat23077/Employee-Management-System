from django.contrib import admin
from employee.models import Employee, Attendance, Notice, workAssignments, Requests

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('eID', 'firstName', 'lastName', 'designation', 'email', 'phoneNo', 'joinDate')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('eId', 'month', 'days')

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('Id', 'title', 'publishDate')

@admin.register(workAssignments)
class WorkAssignmentsAdmin(admin.ModelAdmin):
    list_display = ('Id', 'assignerId', 'taskerId', 'assignDate', 'dueDate')

@admin.register(Requests)
class RequestsAdmin(admin.ModelAdmin):
    list_display = ('Id', 'requesterId', 'destinationEmployeeId', 'requestDate')
