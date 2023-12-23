from django.http import HttpResponse
from django.shortcuts import render

from .models import Country, Region


# Create your views here.
def my_test_view(request):
    return HttpResponse('Hello World !')


def hello_templated(request):
    countries_qs = Country.objects.all()

    # Récupère le Country ayant "1" comme Primary Key
    # .get() raise une erreur si aucun résultat n'est trouvé.
    # france_qs = Country.objects.get(pk=1)

    # .filter() renvoie une liste même s'il n'y a qu'un seul résultat.
    # .filter() ne renvoie pas d'erreur s'il n'y a aucun résultat
    # france_qs = Country.objects.filter(name='France').first()

    # Récupére la première instance de Country trouvée
    # first_country = Country.objects.all().first()
    return render(
        request,
        'hello.html',
        {
            'countries': countries_qs,
        }
    )


#
# def animals(request):
#
#     return HttpResponse('Hello World !')