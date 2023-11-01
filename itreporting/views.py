from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request, 'itreporting/home.html', {'title': 'Home'})

def about(request):

    return render(request, 'itreporting/about.html', {'title': 'About Us'})
def contact(request):

    return render(request, 'itreporting/contacts.html', {'title': 'Contact Us'})
