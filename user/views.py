from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-index')
    else:
        form = CreateUserForm(request.POST)
    context = {
        'form': form,
    }
    return render(request,'user/register.html',context)


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard-index')
#     else:
#         form = UserCreationForm(request.POST)    
#     context = {
#         'form':form,  
#     }
#     return render(request,'user/register.html',context)