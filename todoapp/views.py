from django.shortcuts import render, redirect
from .models import TodoDatabase
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User


def todopage(request):
    todo1 = TodoDatabase.objects.filter(owner = request.user)
    context = {'todokey': todo1}
    if request.user.is_authenticated:
        return render(request, 'todoapp/index.html', context)
    else:
        return redirect('authpage')

def addtask(request):
    owner_var = request.user
    title_var = request.POST.get('title')
    desc_var = request.POST.get('description')
    deadline_var = request.POST.get('deadline')
    to_do_database = TodoDatabase(owner = owner_var, title = title_var, description = desc_var, deadline = deadline_var)
    to_do_database.save()
    return redirect('todomain')

def deletetask(request):
    del_id = request.POST.get('id')
    del_2 = TodoDatabase.objects.get(id = del_id)
    del_2.delete()
    return redirect('todomain')

def deleteall(request):
    TodoDatabase.objects.filter(owner = request.user).delete()
    # for i in del_all:
    #     i.delete()
    return redirect('todomain')

def details(request, pk):
    details1 = TodoDatabase.objects.get(id = pk)
    context = {'tododetails': details1}
    return render(request, 'todoapp/details.html', context)

def update(request, pk):
    update1 = TodoDatabase.objects.get(id = pk)
    context = {'tododetails': update1}
    # title_var = request.POST.get('title')
    # desc_var = request.POST.get('description')
    # deadline_var = request.POST.get('deadline')
    # to_do_database = TodoDatabase(title = title_var, description = desc_var, deadline = deadline_var)
    # to_do_database.save()
    return render(request, 'todoapp/Update.html', context)

def updatetask(request, pk):
    updatetask1 = TodoDatabase.objects.get(id = pk)
    updatetask1.title = request.POST.get('title')
    updatetask1.description = request.POST.get('description')
    updatetask1.deadline = request.POST.get('deadline')
    print(request.POST.get('deadline'))
    updatetask1.save()
    return redirect('update', pk)

def userlogout(request):
    logout(request)
    return redirect('authpage')

def authpage(request):
    return render(request, 'todoapp/loginpage.html')

# def userlogin(request):
#     return render(request, 'todoapp/loginpage.html')

def loginaction(request):
    username_var = request.POST.get('username')
    password_var = request.POST.get('password')
    auth_var = authenticate(request, username = username_var, password = password_var)
    if auth_var is not None:
        login(request, auth_var)
        return redirect('todomain')
    else:
        return redirect('authpage')



def signup(request):
    return render(request, 'todoapp/signup.html')


def signupaction(request):
    username_var = request.POST.get('username')
    email_var = request.POST.get('email')
    password_var = request.POST.get('password')
    user_data = User.objects.create_user(username = username_var, email = email_var, password = password_var)
    return redirect('authpage')












# Create your views here.

