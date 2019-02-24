from django.shortcuts import render, get_object_or_404, render_to_response
from django.views import View

from .models import (
    Instructor,
    Section,
    Course,
    Semester,
    Student,
    Registration,

)

# def instructor_list_view(request):
#     #what comes from the broswer is called request, what we send back is called response
#     #build a list
#     instructor_list = Instructor.objects.all()
#     #instructor_list = Instructor.objects.none()
#     #not Context class.
#     #find template from loader
#     template = loader.get_template('courseinfo/instructor_list.html')
#     #dictionary
#     context = {'instructor_list': instructor_list}
#     #pass the context and get string output
#     output = template.render(context)
#     #send the response to the broswer contain output
#     return HttpResponse(output)


#class based code

class InstructorList(View):
#control+return to import

        def get(self, request):
            return render(
                request,
                'courseinfo/instructor_list.html',
                {'instructor_list': Instructor.objects.all()}
            )


class InstructorDetail(View):
        # pk is an interger(primary key)
        def get(self, request, pk):
            #get an object or return 404
            instructor = get_object_or_404(
                Instructor,
                #pk came in
                pk=pk
            )
            #instructor is related to
            section_list = instructor.sections.all()
            #render a page, template page and context
            return render_to_response(
                #template page
                'courseinfo/instructor_detail.html',
                #context(dictionary)
                {'instructor': instructor, 'section_list': section_list}
            )


class SectionList(View):
        def get(self, request):
            return render(
                request,
                'courseinfo/section_list.html',
                {'section_list': Section.objects.all()}
            )

class SectionDetail(View):

    def get(self, request, pk):
        section = get_object_or_404(
            Section,
            pk=pk
        )
        semester = section.semester
        course = section.course
        instructor = section.instructor
        #'registrations' this name should be the same in models
        registration_list = section.registrations.all()
        return render_to_response(
            'courseinfo/section_detail.html',
            {'section': section,
             'semester': semester,
             'course': course,
             'instructor': instructor,
             'registration_list': registration_list}
        )



class CourseList(View):
        def get(self, request):
            return render(
                request,
                'courseinfo/course_list.html',
                {'course_list': Course.objects.all()}
            )


class CourseDetail(View):

    def get(self, request, pk):
        course = get_object_or_404(
            Course,
            pk=pk
        )
        section_list = course.sections.all()
        return render_to_response(
            'courseinfo/course_detail.html',
            {'course': course,
             'section_list': section_list}
        )


class SemesterList(View):
    def get(self, request):
        return render(
            request,
            'courseinfo/semester_list.html',
            {'semester_list': Semester.objects.all()}
        )



class SemesterDetail(View):

    def get(self, request, pk):
        semester = get_object_or_404(
            Semester,
            pk=pk
        )
        section_list = semester.sections.all()
        return render_to_response(
            'courseinfo/semester_detail.html',
            {'semester': semester,
             'section_list': section_list}
        )


class StudentList(View):
    def get(self, request):
        return render(
            request,
            'courseinfo/student_list.html',
            {'student_list': Student.objects.all()}
        )


class StudentDetail(View):

    def get(self, request, pk):
        student = get_object_or_404(
            Student,
            pk=pk
        )
        registration_list = student.registrations.all()
        return render_to_response(
            'courseinfo/student_detail.html',
            {'student': student,
             'registration_list': registration_list}
        )



class RegistrationList(View):
    def get(self, request):
        return render(
            request,
            'courseinfo/registration_list.html',
            {'registration_list': Registration.objects.all()}
        )

class RegistrationDetail(View):

    def get(self, request, pk):
        registration = get_object_or_404(
            Registration,
            pk=pk
        )
        student = registration.student
        section = registration.section
        return render_to_response(
            'courseinfo/registration_detail.html',
            {'registration': registration,
             'student': student,
             'section': section}
        )


