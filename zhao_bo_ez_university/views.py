from django.shortcuts import redirect

#redirect to list with a click
def redirect_root_view(request):
    return redirect('courseinfo_section_list_urlpattern')
