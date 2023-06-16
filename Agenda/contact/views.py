from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def index(request, letter = None):
    if letter is not None:
        contacts = Contact.objects.filter(name__istartswith=letter)
    else:
        contacts = Contact.objects.filter(name__icontains=request.GET.get('search', ''))
    return render(request, 'contact/index.html', {'contacts': contacts})

def view(request, id):
    contact = Contact.objects.get(id=id)
    context = {
        'contact': contact
    }
    return render(request, 'contact/detail.html', context)


def edit(request, id):
    contact = Contact.objects.get(id=id)

    if(request.method == 'GET'):
        form = ContactForm(instance=contact)
        context = {
            'form': form,
            'id':id
        }
        return render(request, 'contact/edit.html', context)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contacto actualizado.')
            return redirect('contact')


def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha creado el contacto')
            return redirect('contact')  # Redirige a la lista de contactos o a otra URL de tu elección
    else:
        form = ContactForm()
    
    context = {
        'form': form
    }
    return render(request, 'contact/create.html', context)

def delete(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    messages.success(request, 'Contacto eliminado.')
    return redirect('contact')