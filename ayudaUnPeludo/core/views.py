from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'core/index.html')

def adopcionGatos(request):
  cards = [
    {
      "id": 1,
      "nombre": "Ginger",
      "biografia": "Este es Ginger, tiene 6 meses, es amoroso y le gusta ronronear a todo el mundo.",
      "fotografia": "Ginger.jpg",
    },
    {
      "id": 2,
      "nombre": "Lucifer",
      "biografia": "Este es Lucifer, tiene 4 años, es un gato bastante perezoso y dormilón, le gusta ser acariciado mientras duerme.",
      "fotografia": "Lucifer.jpg",
    },
    {
      "id": 3,
      "nombre": "Tommy",
      "biografia": "Este es Tommy, tiene 2 años, es muy juguetón y se lleva muy bien con otros animales, le gusta jugar con una pelota.",
      "fotografia": "Tommy.jpg",
    },
    {
      "id": 4,
      "nombre": "Bola de Nieve",
      "biografia": "Esta Bola de nieve, tiene 3 años, es una gata muy elegante y sofisticada, esta adora ser peinada y amasar a quien lo hace.",
      "fotografia": "BolaDeNieve.jpg",
    },
    {
      "id": 5,
      "nombre": "Misifus",
      "biografia": "Este es Misifus, tiene 5 años, este es bastante concentido, ya que le gusta ser acariciado mientras come, duerme o juega, siempre debes tener tiempo para él.",
      "fotografia": "Misifus.jpg",
    },
    {
      "id": 6,
      "nombre": "Pipina",
      "biografia": "Esta es Pipina, tiene 3 años, le gusta jugar y comer pero lo mas le encanta es dormir con aquellos que quiere. Su comida favorita es el pollo.",
      "fotografia": "Pipina.jpg",
    },
    {
      "id": 7,
      "nombre": "Poncho",
      "biografia": "Este es Poncho, tiene 7 años, este es gruñon y arisco, pero cuando se siente comodo puede ser el gato mas tierno del mundo.",
      "fotografia": "Poncho.jpg",
    },
    {
      "id": 8,
      "nombre": "Yoko",
      "biografia": "Esta es Yoko, tiene 1 año, su aspecto es un tanto peculiar, pero no te dejes engañar, ya que es la mas tierna, regalona y juguetona al igual que una muy buena compañia.",
      "fotografia": "Yoko.jpg",
    },
  ]

  return render(request, 'core/adopcionGatos.html', context= {"cards": cards})

def adopcionPerros(request):
  cards = [
    {
      "id": 1,
      "nombre": "Cachulo",
      "biografia": "Este es Cachulo, tiene 3 años de edad, es muy juguetón, le encanta correr y jugar con peluches. Su comida favorita es la carne de vacuno.",
      "fotografia": "Cachulo.jpg",
    },
    {
      "id": 2,
      "nombre": "Flaca",
      "biografia": "Esta es Flaca, tiene 6 meses de edad, es muy timida y le cuesta darse con los demas, le encanta correr. Su comida favorita son las galletas para perros.",
      "fotografia": "Flaca.jpg",
    },
    {
      "id": 3,
      "nombre": "Nina",
      "biografia": "Esta es Nina, tiene 6 años de edad, es muy Temperamental y territorial, Le gusta bastante dormir. Posee gusto para todas las comidas.",
      "fotografia": "Nina.jpg",
    },
    {
      "id": 4,
      "nombre": "Bolt",
      "biografia": "Este es Bolt, Tiene 8 meses de edad y su nombre está basado en el personaje de la pelicula, este es muy juguetón y muy confianzudo. Le encanta dormir en el sofá.",
      "fotografia": "Bolt.jpg",
    },
    {
      "id": 5,
      "nombre": "Ivo",
      "biografia": "Este es Ivo, Tiene 9 meses de edad, este perrito fue encontrado en la calle por su ex familia, aún está en proceso de rehabilitación, pero listo para entregar amor.",
      "fotografia": "Ivo.jpg",
    },
    {
      "id": 6,
      "nombre": "Magnus",
      "biografia": "Este es Magnus, Tiene 3 meses de edad, este perrito al ser un recien nacido es muy miedoso y no conoce nada del mundo, pero está a la espera de una familia que lo quiera!!.",
      "fotografia": "Magnus.jpg",
    },
    {
      "id": 7,
      "nombre": "Rudolf",
      "biografia": "Este es Rudolf, tiene 5 años, este perrito llego a nuestras sede para el día de navidad, de por si no tenía un hogar y ahora está a la espera de alguien que lo quiera, es muy tierno y amoroso.",
      "fotografia": "Rudolf.jpg",
    },
    {
      "id": 8,
      "nombre": "Thor",
      "biografia": "Este es Thor, Tiene cerca de 9 años, es un ex perro callejero que en estos momentos está en rehabilitación debido a sus heridas y mal cuidados que este tenía al momento de llegar.",
      "fotografia": "Thor.jpg",
    }
  ]

  return render(request, 'core/adopcionPerros.html', context = {"cards": cards})

def comoAdoptar(request):
  return render(request, 'core/comoAdoptar.html')

def donativos(request):
  return render(request, 'core/donativos.html')

def perroBolt(request):
  return render(request, 'core/perros/bolt.html')

def perroCachulo(request):
  return render(request, 'core/perros/cachulo.html')

def perroFlaca(request):
  return render(request, 'core/perros/flaca.html')

def perroIvo(request):
  return render(request, 'core/perros/ivo.html')

def perroMagnus(request):
  return render(request, 'core/perros/magnus.html')

def perroNina(request):
  return render(request, 'core/perros/nina.html')

def perroRudolf(request):
  return render(request, 'core/perros/rudolf.html')

def perroThor(request):
  return render(request, 'core/perros/thor.html')