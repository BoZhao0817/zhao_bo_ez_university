from django.db import models
from django.urls import reverse


# Create your models here.
#tables in database represent by model.class

class Semester(models.Model):
    semester_id = models.AutoField(primary_key=True)
    semester_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % self.semester_name
        #'%s' single string

    def get_absolute_url(self):
        return reverse('courseinfo_semester_detail_urlpattern',
                       kwargs={'pk':self.pk}
                       )

    class Meta:
        ordering = ['semester_name']



class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_number = models.CharField(max_length=20)
    course_name = models.CharField(max_length=225)

    def __str__(self):
        return '%s - %s' % (self.course_number, self.course_name)
        #overwrite the original one is object 1,2,3

    def get_absolute_url(self):
        return reverse('courseinfo_course_detail_urlpattern',
                       kwargs={'pk':self.pk}
                       )




    #internal class
    class Meta:
        # display by its course num
        ordering = ['course_number', 'course_name']
        # make coursenum and coursename unique
        unique_together = (('course_number','course_name'),)


class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse('courseinfo_instructor_detail_urlpattern',
                       kwargs={'pk':self.pk}
                       )


    class Meta:
        ordering = ['last_name', 'first_name']
        unique_together = (('last_name','first_name'),)


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    nickname = models.CharField(max_length=45, blank=True, default='')
    #if not has a value, put an empty string''

    def __str__(self):
        #initialize?
        result = ''
        if self.nickname == '':
            result = '%s, %s' % (self.last_name, self.first_name)
        else:
            result = '%s, %s (%s)' % (self.last_name, self.first_name, self.nickname)
        return result
    
    def get_absolute_url(self):
        return reverse('courseinfo_student_detail_urlpattern',
                       kwargs={'pk':self.pk}
                       )

    class Meta:
        ordering = ['last_name', 'first_name', 'nickname']
        unique_together =(('last_name','first_name','nickname'),)


class Section(models.Model):
    section_id = models.AutoField(primary_key=True)
    section_name = models.CharField(max_length=10)
    semester = models.ForeignKey(Semester, related_name='sections', on_delete=models.PROTECT)
    course = models.ForeignKey(Course, related_name='sections', on_delete=models.PROTECT)
    #instructor foreig key
    instructor = models.ForeignKey(Instructor, related_name='sections', on_delete=models.PROTECT)
    #why related name = sections view the object? other side?

    def __str__(self):
        return '%s - %s (%s)' % (self.course.course_number, self.section_name, self.semester.semester_name)

    def get_absolute_url(self):
        return reverse('courseinfo_section_detail_urlpattern',
                       kwargs={'pk':self.pk}
                       )


    class Meta:
        ordering = ['course__course_number','section_name', 'semester__semester_name']

class Registration(models.Model):
    registration_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, related_name='registrations', on_delete=models.PROTECT)
    section = models.ForeignKey(Section, related_name='registrations', on_delete=models.PROTECT)


    def __str__(self):
        return '%s / %s' % (self.section, self.student)

    def get_absolute_url(self):
        return reverse('courseinfo_registration_detail_urlpattern',
                       kwargs={'pk':self.pk}
                       )

    class Meta:
        ordering = ['section', 'student']
        #only can register one time in one course
        unique_together = (('section', 'student'),)
#run migrate build database table that related to models.py






