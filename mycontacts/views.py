from django.shortcuts import render
from .forms import AddForm
from .models import Contact
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404


def deletar_usuario(request, id):
    usuario = get_object_or_404(Contact, id=id)
    usuario.delete()
    return redirect('/')

def verDetalhes(request, id):
    usuario = get_object_or_404(Contact, id=id)

    if request.method == "GET":

        novo_nome = request.GET.get('name')
        novo_relation = request.GET.get('relation')
        novo_phone = request.GET.get('phone')
        novo_email = request.GET.get('email')

        return render(request, 'mycontacts/verDetalhes.html', {'usuario': usuario})    

def editarContato(request, id):
    usuario = get_object_or_404(Contact, id=id)

    if request.method == "POST":

        novo_nome = request.POST.get('name')
        novo_relation = request.POST.get('relation')
        novo_phone = request.POST.get('phone')
        novo_email = request.POST.get('email')

        usuario.name = novo_nome
        usuario.relation = novo_relation
        usuario.phone = novo_phone
        usuario.email = novo_email

        usuario.save()

        return redirect('/')
    
    return render(request, 'mycontacts/editarContato.html', {'usuario': usuario})

def adicionar(request):
    """ This function is called to add one contact member to your contact list in your Database """
    if request.method == 'POST':
        
        django_form = AddForm(request.POST)
        if django_form.is_valid():
           
            """ Assign data in Django Form to local variables """
            new_member_name = django_form.data.get("name")
            new_member_relation = django_form.data.get("relation")
            new_member_phone = django_form.data.get('phone')
            new_member_email = django_form.data.get('email')
            
            """ This is how your model connects to database and create a new member """
            Contact.objects.create(
                name =  new_member_name, 
                relation = new_member_relation,
                phone = new_member_phone,
                email = new_member_email, 
                )
                 
            contact_list = Contact.objects.all()
            return render(request, 'mycontacts/mycontacts.html',{'contacts': contact_list}) 
        
        else:
            """ redirect to the same page if django_form goes wrong """
            return render(request, 'mycontacts/adicionar.html')
    else:
        return render(request, 'mycontacts/adicionar.html')


def mycontacts(request):
    contact_list = Contact.objects.all()
    return render(request, 'mycontacts/mycontacts.html',{'contacts': contact_list})