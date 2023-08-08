from django.urls import path

from users.views import login, registation

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registation, name='registration'),

]
