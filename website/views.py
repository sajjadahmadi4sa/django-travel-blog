from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .models import Contact
from django.contrib import messages

def index_view (request):
    return render (request,'website/index.html')

def about_view (request):
    return render (request,'website/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],)

            messages.success(request,'Your message was sent successfully!')
            form = ContactForm()
        else:
            messages.error(request,'Please correct the errors and try again.')
    else:
        form = ContactForm()
    return render(request,'website/contact.html',{'form': form})