from django.conf.urls import include, url
from django.contrib import admin
from app import views
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings 



urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^location/', 'app.views.location'),
    url(r'^login', 'app.views.login_view'),
    url(r'^signup_view', 'app.views.sign_up'),
    url(r'^logout_view', 'app.views.logout_view'),
    url(r'^timeslots/', 'app.views.timeslots'),
    url(r'^timeslots/(?P<pk>\d+)/', 'app.views.timeslots'),
    url(r'^order_confirmation/', 'app.views.order_confirmation'),
    url(r'^homepage/', 'app.views.homepage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

