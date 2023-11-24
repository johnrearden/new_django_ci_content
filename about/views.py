from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateRequestForm

def about(request):
    coder = About.objects.order_by('-updated_on').first()

    collaborate_form = CollaborateRequestForm()

    if request.method == "POST":
        collaborate_form = CollaborateRequestForm(data=request.POST)
        if collaborate_form.is_valid:
            collaborate_form.save()
            messages.add_message(
                request,
                messages.SUCCESS, 
                'Thanks for your request for collaboration!')
    return render(
        request,
        'about/about.html',
        {
            'coder': coder,
            'collaborate_form': collaborate_form,
        }
    )
    


