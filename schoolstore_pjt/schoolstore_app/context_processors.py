# context_processors.py

from .models import Department,Course

def departments_list(request):
    departments = Department.objects.all()
    return {'departments_list': departments}

def courses_list(request):
    courses = Course.objects.all()
    return {'course_list': courses}
