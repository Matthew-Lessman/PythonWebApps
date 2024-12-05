from django.views.generic import RedirectView
from django.urls import path

from photos.views import PhotoDetailView, PhotoListView


# urlpatterns = [

#     # Home
#     path('', RedirectView.as_view(url='photo/')),

#     # Photos
#     path('photo/', PhotoListView.as_view()),
#     path('photo/<int:id>', PhotoDetailView.as_view()),
# ]

urlpatterns = [
    path('', PhotoListView.as_view(), name='photo_list'),
    path('detail/<str:id>/', PhotoDetailView.as_view(), name='photo_detail'),  # Match this name
]
