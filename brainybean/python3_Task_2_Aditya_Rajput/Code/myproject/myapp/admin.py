from django.contrib import admin
from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    site_header = "Custom Admin Panel"
    site_title = "Admin | My Project"
    index_title = "Welcome to My Project Admin"

    def each_context(self, request):
        context = super().each_context(request)
        context['custom_css'] = 'css/custom_admin.css'
        return context

admin.site = CustomAdminSite()

# Register models as usual
from .models import MyModel
admin.site.register(MyModel)

# Add CSS to admin
def custom_css(request):
    from django.conf import settings
    from django.http import HttpResponse
    from django.template.loader import render_to_string

    css_content = render_to_string('static/css/custom_admin.css')
    return HttpResponse(css_content, content_type='text/css')

# admin.site.register_view('custom-admin-css', view=custom_css, name='custom_admin_css')

admin.site.site_url = '/home/'  # Redirects to homepage from admin
