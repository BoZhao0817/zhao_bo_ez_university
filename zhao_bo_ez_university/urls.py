from django.contrib import admin
from django.urls import path
from courseinfo.views import (
    instructor_list_view,
    section_list_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('instructor/', instructor_list_view),
    path('section/', section_list_view),
    # course
    # semester
    # student
    # registration
]
