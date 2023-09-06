from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
# def index(req):
#     forma = Personforma()
#     bd = Person.objects.all()
#     print(bd)
#     print('===============================')
#     print(Person.objects.get(id=22).name, Person.objects.get(id=22).age)
#     print('===============================')
#     for p in Person.objects.all():
#         print(p.name, p.age, p.id)
#     print('===============================')
#     igors = Person.objects.filter(name='Igor')
#     print(igors.values())
#     print(igors.values_list())
#     print(igors.in_bulk())
#     print('id игоря',igors[0].id)
#     print('==================================')
#     qqq = Person.objects.exclude(name='Vlad')
#     print(qqq.values_list())
#     www = Person.objects.filter(name='Igor').exclude(age=22)
#     print(www.values_list())
#     print('==================================')
#     print(Person.objects.filter(name='Igor'))
#     k1 = Product.objects.create(title='confeta', price=50.00, company_id=2)
#     k2 = Product.objects.create(title='confetaBIG', price=15.00, company_id=2)
#     print(k2.company.name)
#     shokoladki = Product.objects.filter(company__name='MARS')
#     print(shokoladki.values_list())
#     data = {'forma':forma, 'database':bd}
#     return render(req,'index.html', context=data)
#
#     pass
#
# def add1(req):
#     man = Person()
#     man.name='Igor'
#     man.age = 22
#     man.save()
#     man2 = Person.objects.create(name='Vlad', age=13)
#     return redirect('home')    #назввание маршрута
#
# def create(req):
#     if req.POST:
#         man = Person()
#         man.name = req.POST.get('name1')
#         man.age = req.POST.get('age1')
#         man.save()
#         return redirect('home')
#     pass
#
# def delete(req,ids):
#     man = Person.objects.get(id=ids)
#     man.delete()
#     return redirect('home')
#
# def edit(req,ids):
#     man = Person.objects.get(id=ids)
#     anketa = Personforma()
#     data = {'forma':anketa}
#     if req.POST:
#         man.name = req.POST['name1']
#         man.age = req.POST['age1']
#         man.save()
#         return redirect('home')
#     else:
#         return render(req,'edit.html', context=data)
#     pass

# def indexx(req):
#     forma = Carforma()
#     bd = Car.objects.all()
#     data = {'forma':forma, 'database':bd}
#     return render(req,'index.html', context=data)
#     pass
#
# def add2(req):
#     avto = Car()
#     avto.marka='M3'
#     avto.proizv='BMW'
#     avto.age = 2015
#     avto.gn = 'M364MM'
#     avto.save()
#     avto2 = Car.objects.create(marka='ELIS', proizv='LOTUS', age=2018, gn='C896AA')
#     return redirect('home')    #назввание маршрута
#
# def create2(req):
#     if req.POST:
#         avto = Car()
#         avto.marka = req.POST.get('marka1')
#         avto.proizv = req.POST.get('proizv1')
#         avto.age = req.POST.get('age1')
#         avto.gn = req.POST.get('gn1')
#         avto.save()
#         return redirect('home')
#     pass
#
# def delete2(req,ids):
#     avto = Car.objects.get(id=ids)
#     avto.delete()
#     return redirect('home')

def film(req):
    forma = Personforma()
    films = Film.objects.all()
    data = {'forma':forma, 'database':films}
    return render(req, 'index.html', context=data)

def films_filter(req):
    country = req.GET.get('country')
    year = req.GET.get('year')

    films = Film.objects.all()

    if country:
        films = films.filter(country=country)

    if year:
        films = films.filter(year=year)

    if country and year:
        # Получаем список фильмов данной страны, за исключением фильмов данного года
        films_excluded_year = Film.objects.filter(country=country).exclude(year=year)
    else:
        films_excluded_year = None

    data = {'films': films, 'films_excluded_year': films_excluded_year}
    return render(req, 'index.html', context=data)
