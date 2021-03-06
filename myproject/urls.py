
"""example URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from employee.views import EmployeeImage, EmpImageDisplay
from home.views import HomePageView

urlpatterns = [
    # path('', HomePageView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace = 'home')),
    # path('', EmployeeImage.as_view(), name='emp_image.html'),
    # path('upload/<int:pk>/', EmpImageDisplay.as_view(), name='emp_image_display'),
]

urlpatterns += staticfiles_urlpatterns()

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)