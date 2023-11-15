from django.shortcuts import render
from .models import About

def about(request):
    coder = About.objects.order_by('-updated_on').first()
    return render(
        request,
        'about/about.html',
        {'coder': coder}
    )
    


