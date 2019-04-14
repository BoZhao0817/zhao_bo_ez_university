from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import RedirectView, TemplateView

from zhao_bo_ez_university.views import redirect_root_view

urlpatterns = [

    # to seperate the urls
    path('',
         RedirectView.as_view(
             pattern_name='about_urlpattern',
             permanent=False
         )),

    path('login/',
         LoginView.as_view(template_name='courseinfo/login.html'),
         name='login_urlpattern'
         ),

    path('logout/',
         LogoutView.as_view(),
         name='logout_urlpattern'
         ),

    # no data only with a template wiew?
    path('about/',
         TemplateView.as_view(
             template_name='courseinfo/about.html'),
         name='about_urlpattern'
         ),

    path('admin/', admin.site.urls),

    path('', include('courseinfo.urls'))

]
