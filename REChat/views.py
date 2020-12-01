
from django.shortcuts import render
from .forms import contactForm


def home(request):
  title = 'nigga cat'
  return render(request, 'home.html', {'title': title})


def hacking(request):
  return render(request, 'hack.html', {'title': 'hacking hehe'})


def about(request):
  if request.user.is_authenticated:
    my_list = ['nigga', 'is', 'good']
  return render(request, 'about.html', {'my_list': my_list})


def contact(request):
  form = contactForm(request.POST or None)
  if form.is_valid():
    print(form.cleaned_data)
    form = contactForm()
  context = {
    'title': 'Contact',
    'form': form
  }
  return render(request, 'form.html', context)


def calculator(request):
  return render(request, 'calculator.html')