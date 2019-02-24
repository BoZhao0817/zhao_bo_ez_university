from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #to seperate the urls
    path('admin/', admin.site.urls),
    path('', include('courseinfo.urls'))

]
