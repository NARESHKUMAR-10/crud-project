from django.shortcuts import render, redirect
from .models import Contact

# READ: Show all contacts
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'myapp/list.html', {'contacts': contacts})

# CREATE: Add contact
def add_contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        Contact.objects.create(name=name, phone=phone)
        return redirect('/')
    return render(request, 'myapp/add.html')

# UPDATE: Edit contact
def edit_contact(request, id):
    contact = Contact.objects.get(id=id)
    if request.method == 'POST':
        contact.name = request.POST['name']
        contact.phone = request.POST['phone']
        contact.save()
        return redirect('/')
    return render(request, 'myapp/edit.html', {'contact': contact})

# DELETE: Remove contact
def delete_contact(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('/')

# Create your views here.
