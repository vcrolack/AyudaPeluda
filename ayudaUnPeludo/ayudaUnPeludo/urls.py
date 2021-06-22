"""ayudaUnPeludo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('adopcionGatos/', include('core.urls')),
    path('aopcionPerros/', include('core.urls')),
    path('comoAdoptar/', include('core.urls')),
    path('donativos/', include('core.urls')),
    path('perroBolt/', include('core.urls')),
    path('perroCachulo/', include('core.urls')),
    path('perroFlaca/', include('core.urls')),
    path('perroIvo/', include('core.urls')),
    path('perroMagnus/', include('core.urls')),
    path('perroNina/', include('core.urls')),
    path('perroRudolf/', include('core.urls')),
]
