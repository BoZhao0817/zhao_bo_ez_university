from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader

from .models import (
    Instructor,
    Section,
)

def instructor_list_view(request):
    #what comes from the broswer is called request, what we send back is called response
    #build a list
    instructor_list = Instructor.objects.all()
    #instructor_list = Instructor.objects.none()
    #not Context class.
    #find template from loader
    template = loader.get_template('courseinfo/instructor_list.html')
    #dictionary
    context = {'instructor_list': instructor_list}
    #pass the context and get string output
    output = template.render(context)
    #send the response to the broswer contain output
    return HttpResponse(output)


def section_list_view(request):
    section_list = Section.objects.all()
    template = loader.get_template('courseinfo/section_list.html')
    context = {'section_list': section_list}
    output = template.render(context)
    return HttpResponse(output)

