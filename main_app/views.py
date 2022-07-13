from urllib import request, response
from django.shortcuts import redirect, render
import requests

from django.views.generic import ListView, DetailView
# Add the two imports below
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import UserCreationForm
# Import the login_required decorator
from django.contrib.auth.decorators import login_required

# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Anime

# Create your views here.


# anime_name = input("")
# response = requests.get(f'https://api.jikan.moe/v4/anime?letter={anime_name}')
# data = response.json()
# print(data['naruto'])
def searchbar(request):
  if request.method == 'GET':
    user_input = request.GET.get('search')
    response = requests.get(f'https://api.jikan.moe/v4/anime?q={user_input}')
    data = response.json()['data'][0]
    print(data['title'])
    return render (request, 'search.html', {'data': data})




def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def animes_index(request):
    anime = Anime.objects.filter(user=request.user)
    return render(request, 'animes/index.html', {'animes': anime})


def animes_detail(request, anime_id):
    anime = Anime.objects.get(id=anime_id)
    return render(request, 'animes/detail.html', {'animes': anime})



def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


class AnimeCreate(CreateView):
   model = Anime
   fields = ['name','description', 'year']
   success_url = '/animes/'

   def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
    
class AnimeUpdate(UpdateView):
    model = Anime
    fields = ['description']


class AnimeDelete(DeleteView):
    model = Anime
    success_url = '/animes'