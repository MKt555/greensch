from django.shortcuts import render, redirect
from academy.forms import DocumentForm
from django.http import HttpResponse

# Create your views here.
def academyscreen_view(request):
    print(request.headers)
    return render(request, "academy/academy.html", {})#references home.html
#context is used to get some values or variables from the database


#def Schools_list(request):
    #return 


#def SchoolsForm(request):
    #'''Insert and Delete Operation.'''
    #return    

#def SchoolDelete(request):
    #return

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('academy')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })