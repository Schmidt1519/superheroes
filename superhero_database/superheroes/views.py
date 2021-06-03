from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Superhero
from django.urls import reverse
# Create your views here.


def index(request):
    all_superheroes = Superhero.objects.all()
    context = {"all_superheroes": all_superheroes}
    return render(request, 'superheroes/index.html', context)


def detail(request, superhero_id):
    superhero_detail = Superhero.objects.get(id=superhero_id)
    context = {"superhero_detail": superhero_detail}
    return render(request, 'superheroes/detail.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        catchphrase = request.POST.get('catchphrase')
        new_superhero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary_ability, secondary_ability=secondary_ability, catchphrase=catchphrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')


def edit(request, superhero_id):
    superhero_edit_detail = Superhero.objects.get(id=superhero_id)
    context = {"superhero_edit_detail": superhero_edit_detail}

    if request.method == 'POST':
        superhero_edit = Superhero.objects.get(id=superhero_id)
        superhero_edit.name = request.POST.get('name')
        superhero_edit.alter_ego = request.POST.get('alter_ego')
        superhero_edit.primary_ability = request.POST.get('primary_ability')
        superhero_edit.secondary_ability = request.POST.get('secondary_ability')
        superhero_edit.catchphrase = request.POST.get('catchphrase')
        superhero_edit.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/edit.html', context)


def delete(request, superhero_id):
    superhero_delete_detail = Superhero.objects.get(id=superhero_id)
    context = {"superhero_delete_detail": superhero_delete_detail}

    if request.method == 'POST':
        superhero_delete = Superhero.objects.get(id=superhero_id)
        superhero_delete.delete()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/delete.html', context)