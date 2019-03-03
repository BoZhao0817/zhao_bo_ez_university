from django.contrib import admin
from django.urls import path, include
from zhao_bo_ez_university.views import redirect_root_view

urlpatterns = [
    #to seperate the urls
    path('', redirect_root_view),
    path('admin/', admin.site.urls),
    path('', include('courseinfo.urls'))

]
