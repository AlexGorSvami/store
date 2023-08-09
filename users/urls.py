from django.urls import path

from users.views import login, registation, profile, logout

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registation, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout')

]
