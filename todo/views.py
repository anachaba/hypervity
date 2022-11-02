from audioop import reverse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView,UpdateView
from django.urls import reverse_lazy


from .models import Activity


# Create your views here.


class ActivityDetail(ListView):
    model = Activity
    template_name = 'home.html'


class AddTodo(CreateView):
    model = Activity
    template_name = 'Add.html'
    fields = ['name']
    success_url = reverse_lazy('home')


class DeleteTodo(DeleteView):
    model = Activity
    template_name = 'delete.html'
    success_url = reverse_lazy('home')


class UpdateTodo(UpdateView):
    model = Activity
    template_name = 'update.html'
    success_url = reverse_lazy('home')
    fields= ['name']
