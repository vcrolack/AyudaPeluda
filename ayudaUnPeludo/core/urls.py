'''creación de paths para la aplicación core '''
from django.urls import path
from .views import index, adopcionGatos, adopcionPerros, comoAdoptar, donativos, perroBolt

urlpatterns = [
  path('', index, name = "home"),
  path('adopcionGatos/', adopcionGatos, name = "adopcionGatos"),
  path('adopcionPerros/', adopcionPerros, name = "adopcionPerros"),
  path('comoAdoptar/', comoAdoptar, name = "comoAdoptar"),
  path('donativos/', donativos, name = "donativos"),
  path('perroBolt/', perroBolt, name="perroBolt"),
]