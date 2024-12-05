from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView

superheroes = [
    {
        'id': 'Daredevil',
        'name': 'Matt Murdock',
        'image': 'daredevilpic.jpg',
        'strengths': 'Martial Arts, Enhanced Hearing, Smelling, Taste, and Touch',
        'weaknesses': 'Mortal, Blind',
    },
    {
        'id': 'Punisher',
        'name': 'Frank Castle',
        'image': 'punisher.jpg',
        'strengths': 'Excellent Marksman, Military Expert, Advanced Combat, Intellect',
        'weaknesses': 'Mortal, Finite Amount of Ammunition',
    },
    {
        'id': 'Arrow',
        'name': 'Oliver Queen',
        'image': 'arrow.jpg',
        'strengths': 'Martial Arts, Enhanced Hearing, Smelling, Taste, and Touch',
        'weaknesses': 'Mortal, Blind',
    },
    {
        'id': 'Spiderman',
        'name': 'Peter Parker',
        'image': 'spiderman.jpg',
        'strengths': '"Spidey" Senses, Enhanced Physical Attributes (Jumping, Strength, Senses, etc), Healing',
        'weaknesses': 'Ethyl Chloride, Water, Mortal',
    },
    {
        'id': '9 Tails Jinchuriki',
        'name': 'Naruto Uzumaki',
        'image': 'naruto.jpg',
        'strengths': 'Chakra (Energy), Creative Fighting, Durability',
        'weaknesses': 'Mortal, Naive, Immature',
    },
]

# class PhotoListView(TemplateView):
#      template_name = 'photo.html'

#      def get_context_data(self, **kwargs):
#          photos = [{
#                  'name': photo['name'], 
#                  'image': f"/static/images/{photo['image']}"}
#                    for photo in superheroes]
#          return {'photos': photos}
from django.urls import reverse

class PhotoListView(TemplateView):
    template_name = 'photo.html'

    def get_context_data(self, **kwargs):
        photos = [{
            'name': photo['name'],
            'image': f"/static/images/{photo['image']}",
            'url': reverse('photo_detail', kwargs={'id': photo['id']})  # This line generates the link
        } for photo in superheroes]
        return {'photos': photos}

    

class PhotoDetailView(TemplateView):
    template_name = 'photos.html'

    def get_context_data(self, **kwargs):
        id = kwargs['id']

        # Find the superhero by name in the 'superheroes' list
        superhero = next((photo for photo in superheroes if photo['id'] == id), None)

        if superhero:
            context = {
                'name': superhero['name'],
                'image': f"/static/images/{superhero['image']}",
                'strengths': superhero['strengths'],
                'weaknesses': superhero['weaknesses'],
            }
        else:
            # Handle the case where the superhero is not found
            context = {
                'name': 'Superhero Not Found',
                'image': '/static/images/placeholder.jpg',  # Provide a placeholder image
                'strengths': 'N/A',
                'weaknesses': 'N/A',
            }

        return context