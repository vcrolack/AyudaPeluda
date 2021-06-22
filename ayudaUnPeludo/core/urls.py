'''creación de paths para la aplicación core '''
from django.urls import path
from .views import index, adopcionGatos, adopcionPerros, comoAdoptar, donativos, perroBolt, perroCachulo, perroFlaca, perroIvo, perroMagnus, perroNina, perroRudolf, perroThor

urlpatterns = [
  path('', index, name = "home"),
  path('adopcionGatos/', adopcionGatos, name = "adopcionGatos"),
  path('adopcionPerros/', adopcionPerros, name = "adopcionPerros"),
  path('comoAdoptar/', comoAdoptar, name = "comoAdoptar"),
  path('donativos/', donativos, name = "donativos"),
  path('perroBolt/', perroBolt, name="perroBolt"),
  path('perroCachulo/', perroCachulo, name = "perroCachulo"),
  path('perroFlaca/', perroFlaca, name = "perroFlaca"),
  path('perroIvo/', perroIvo, name = "perroIvo"),
  path('perroMagnus/', perroMagnus, name = "perroMagnus"),
  path('perroNina/', perroNina, name = "perroNina"), 
  path('perroRudolf/', perroRudolf, name = "perroRudolf"),
  path('perroThor/', perroThor, name = "perroThor"),
]