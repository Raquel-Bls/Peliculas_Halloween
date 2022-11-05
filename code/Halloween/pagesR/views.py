from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Pelicula
# Create your views here.


class peliculaPageView(ListView):
    template_name = 'pelicula.html'
    model = Pelicula
    context_object_name = 'Todas_Peliculas'


class peliculaPageDetail(DetailView):
    template_name = 'pelicula_detalle.html'
    model = Pelicula
    context_object_name = 'Todas_Peliculas'


class peliculaPageCreate(CreateView):
    template_name = 'pelicula_nuevo.html'
    model = Pelicula
    fields = ('nom_pelicula', 'resumen', 'genero', 'duracion', 'reparto')


class peliculaPageUpdate(UpdateView):
    template_name = 'pelicula_editar.html'
    model = Pelicula
    fields = ['resumen', 'genero', 'reparto']


class peliculaPageDelete(DeleteView):
    template_name = 'pelicula_eliminar.html'
    model = Pelicula
    fields = "_all_"
    success_url = reverse_lazy('pelicula')
