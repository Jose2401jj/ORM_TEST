from library.models import Libro, Autor, AutorCapitulo, Editorial, LibroCronica
from django.db.models import Min, Max, Avg, Count, Sum
from django.db.models import F

# 1. Crea 6 autores y relaciónalos con el libro  “La Fe”. (bulk_create)
autores_la_fe = Autor.objects.bulk_create([
    Autor(nombre="Mario"),
    Autor(nombre="Marco"),
    Autor(nombre="Jose"),
    Autor(nombre="antoni"),
    Autor(nombre="AutorE"),
    Autor(nombre="AutorF")
])

libro_la_fe = Libro.objects.get(titulo="La Fe")

for autor in autores_la_fe:
    autor.libro.add(libro_la_fe)


# 2. Encuentra todos los autores con nombres que contengan la letra "o" y que hayan escrito un libro en la categoría "Referencia".
autores_con_o_referencia = Autor.objects.filter(
    nombre__icontains="o",
    libro__categoria="Referencia"
).distinct()


# 3. Busca libros publicados entre los años 2020 y 2024 y con mas de 250 páginas y tengan una categoría diferente de "Referencia".
libros_2020_2024 = Libro.objects.filter(
    fecha_publicacion__year__range=(2020, 2024),
    paginas__gt=250
).exclude(categoria="Referencia")


#4.  Dado el libro la “la biblia” mostrar todos sus actoresautores_con_o_referencia = Autor.objects.filter(
libro_biblia = Libro.objects.get(titulo="La Biblia")
autores_biblia = libro_biblia.autores.all()

#5. Incrementa el número de páginas en 50 para todos los libros que tengan más de 100 páginas y cuyo autor sea “antoni”
libros_antoni = Libro.objects.filter(
    paginas__gt=100,
    autores__nombre__iexact="antoni"
)
libros_antoni.update(paginas=F('paginas') + 50)