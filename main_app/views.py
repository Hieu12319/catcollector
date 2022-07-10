from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cat

# faux Cat Data - Database simulation
#class Cat:
#    def __init__(self, name, breed, description, age):
#        self.name = name
#        self.breed = breed
#        self.description = description 
#        self.age = age

#cats = [
#    Cat('Lolo', 'tabby', 'foul little demon', 3),
#    Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
#    Cat('Raven', 'black tripod', '3 legged cat', 4)
#]

# Create your views here.

def home(request):
    return HttpResponse('<h1> Hello World /ᐠ｡‸｡ᐟ\ﾉ </h1>')


def about(request):
    # If you want to send back raw textr or an html string use httpresponse
   # return HttpResponse('About Page')
   # If you want to send back a full template file use render
   return render(request, 'about.html')

def cats_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})


def cats_detail(request, cat_id):
    # Get the individual Cat
  cat = Cat.objects.get(id=cat_id)
  #render the template, 
  return render(request, 'cats/detail.html', { 'cat': cat })
#create page
class CatCreate(CreateView):
  model = Cat
  fields = '__all__'
  success_url= '/cats/'

# edit page
class CatUpdate(UpdateView):
  model = Cat
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

  # Delete page
class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats/'
