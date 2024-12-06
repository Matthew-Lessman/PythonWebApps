from pathlib import Path
from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Superhero


class MainView(TemplateView):
    template_name = 'hero.html'


class HeroView(TemplateView):
    template_name = 'heros.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['superhero'] = Superhero.objects.get(name=kwargs['name'])
        except Superhero.DoesNotExist:
            context['error_message'] = "Superhero not found"
        return context