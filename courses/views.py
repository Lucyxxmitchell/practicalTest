from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Courses

# Create your views here.
def index(request):
    courses_list = Courses.objects
    context_dict = {}
    context_dict['courses'] = courses_list

    return render(request, 'courses/index.html', context=context_dict)
