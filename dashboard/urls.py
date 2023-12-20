from django.urls import path
from .views import dashboard, videos_list, blank_page, badges, buttons, cards, card_actions, cards_masonry, colors, form_elements, login

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('login/', login, name="login"),
    path('videos/', videos_list, name="videos"),
    path('blank-page/', blank_page, name="blank-page"),
    path('badges/', badges, name="badges"),
    path('buttons/', buttons, name="buttons"),
    path('cards/', cards, name="cards"),
    path('card-actions/', card_actions, name="card-actions"),
    path('cards-masonry/', cards_masonry, name="cards-masonry"),
    path('colors/', colors, name="colors"),
    path('form-elements/', form_elements, name="form-elements"),
]