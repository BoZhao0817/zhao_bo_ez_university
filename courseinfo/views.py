from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.views import View

from courseinfo.forms import InstructorForm, SectionForm, CourseForm, SemesterForm, StudentForm, RegistrationForm
from courseinfo.utils import ObjectCreateMixin
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
            return render(
                request,
                #template page
                'courseinfo/instructor_detail.html',
                #context(dictionary)
                {'instructor': instructor, 'section_list': section_list}
            )

#mixin a particular class to be a subclass of more than one superclass
class InstructorCreate(ObjectCreateMixin, View):
    #class
    form_class = InstructorForm
    template_name = 'courseinfo/instructor_form.html'


class InstructorUpdate(View):
    form_class = InstructorForm
    model = Instructor
    template_name = 'courseinfo/instructor_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        instructor = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=instructor),
            'instructor': instructor,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        instructor = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=instructor)
        if bound_form.is_valid():
            new_instructor = bound_form.save()
            return redirect(new_instructor)
        else:
            context = {
                'form': bound_form,
                'instructor': instructor
            }
            return render(
                request,
                self.template_name,
                context)


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
        return render(
            request,
            'courseinfo/section_detail.html',
            {'section': section,
             'semester': semester,
             'course': course,
             'instructor': instructor,
             'registration_list': registration_list}
        )

class SectionCreate(ObjectCreateMixin, View):
    #class
    form_class = SectionForm
    template_name = 'courseinfo/section_form.html'

class SectionUpdate(View):
    form_class = SectionForm
    model = Section
    template_name = 'courseinfo/section_form_update.html'

    #data retrtieved
    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        section = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=section),
            'section': section,
        }
        return render(
           request, self.template_name, context)

    def post(self, request, pk):
        section = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=section)
        if bound_form.is_valid():
            new_section = bound_form.save()
            return redirect(new_section)
        else:
            context = {
                'form': bound_form,
                'section': section,
            }
            return render(
                request,
                self.template_name,
                context)


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
        return render(
            request,
            'courseinfo/course_detail.html',
            {'course': course,
             'section_list': section_list}
        )

class CourseCreate(ObjectCreateMixin, View):
    #class
    form_class = CourseForm
    template_name = 'courseinfo/course_form.html'

class CourseUpdate(View):
    form_class = CourseForm
    model = Course
    template_name = 'courseinfo/course_form_update.html'

    #data retrtieved
    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        course = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=course),
            'course': course,
        }
        return render(
           request, self.template_name, context)

    def post(self, request, pk):
        course = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=course)
        if bound_form.is_valid():
            new_course = bound_form.save()
            return redirect(new_course)
        else:
            context = {
                'form': bound_form,
                'section': course,
            }
            return render(
                request,
                self.template_name,
                context)


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
        return render(
            request,
            'courseinfo/semester_detail.html',
            {'semester': semester,
             'section_list': section_list}
        )

class SemesterCreate(ObjectCreateMixin, View):
    #class
    form_class = SemesterForm
    template_name = 'courseinfo/semester_form.html'

class SemesterUpdate(View):
    form_class = SectionForm
    model = Semester
    template_name = 'courseinfo/semester_form_update.html'

    #data retrtieved
    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        semester = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=semester),
            'course': semester,
        }
        return render(
           request, self.template_name, context)

    def post(self, request, pk):
        semester = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=semester)
        if bound_form.is_valid():
            new_semester = bound_form.save()
            return redirect(new_semester)
        else:
            context = {
                'form': bound_form,
                'section': semester,
            }
            return render(
                request,
                self.template_name,
                context)


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
        return render(
            request,
            'courseinfo/student_detail.html',
            {'student': student,
             'registration_list': registration_list}
        )

class StudentCreate(ObjectCreateMixin, View):
    #class
    form_class = StudentForm
    template_name = 'courseinfo/student_form.html'

class StudentUpdate(View):
    form_class = StudentForm
    model = Student
    template_name = 'courseinfo/student_form_update.html'

    #data retrtieved
    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        student = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=student),
            'course': student,
        }
        return render(
           request, self.template_name, context)

    def post(self, request, pk):
        student = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=student)
        if bound_form.is_valid():
            new_student = bound_form.save()
            return redirect(new_student)
        else:
            context = {
                'form': bound_form,
                'section': student,
            }
            return render(
                request,
                self.template_name,
                context)


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
        return render(
            request,
            'courseinfo/registration_detail.html',
            {'registration': registration,
             'student': student,
             'section': section}
        )

class RegistrationCreate(ObjectCreateMixin, View):
    #class
    form_class = RegistrationForm
    template_name = 'courseinfo/registration_form.html'

class RegistrationUpdate(View):
    form_class = RegistrationForm
    model = Registration
    template_name = 'courseinfo/registration_form_update.html'

    #data retrtieved
    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        registration = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=registration),
            'course': registration,
        }
        return render(
           request, self.template_name, context)

    def post(self, request, pk):
        registration = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=registration)
        if bound_form.is_valid():
            new_registration = bound_form.save()
            return redirect(new_registration)
        else:
            context = {
                'form': bound_form,
                'section': registration,
            }
            return render(
                request,
                self.template_name,
                context)


