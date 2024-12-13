# from django.urls import reverse_lazy
# from django.views.generic import TemplateView
# from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.forms import UserCreationForm
# from .models import Superhero

# class SignUpView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'

# class HeroListView(ListView):
#     template_name = 'hero/list.html'
#     model = Superhero


# class HeroDetailView(DetailView):
#     template_name = 'hero/detail.html'
#     model = Superhero


# class HeroCreateView(LoginRequiredMixin, CreateView):
#     template_name = "hero/add.html"
#     model = Superhero
#     fields = '__all__'


# class HeroUpdateView(LoginRequiredMixin, UpdateView):
#     template_name = "hero/edit.html"
#     model = Superhero
#     fields = '__all__'


# class HeroDeleteView(LoginRequiredMixin, DeleteView):
#     model = Superhero
#     template_name = 'hero/delete.html'
#     success_url = reverse_lazy('hero_list')

from django.shortcuts import render

def hero_list(request):
    heroes = [
        {"id": 2, "name": "Frank Castle", "alias": "Punisher"},
        {"id": 3, "name": "Oliver Queen", "alias": "Arrow"},
        {"id": 4, "name": "Peter Parker", "alias": "Spiderman"},
        {"id": 5, "name": "Naruto Uzumaki", "alias": "9 Tails Jinchuriki"},
        {"id": 6, "name": "Matt Murdock", "alias": "Daredevil"},
    ]
    return render(request, 'hero_list.html', {'heroes': heroes})
