from django.shortcuts import render, redirect
from .models import TodoDatabase

def todopage(request):
    todo1 = TodoDatabase.objects.all()
    context = {'todokey': todo1}
    return render(request, 'todoapp/index.html', context)

def addtask(request):
    title_var = request.POST.get('title')
    desc_var = request.POST.get('description')
    deadline_var = request.POST.get('deadline')
    to_do_database = TodoDatabase(title = title_var, description = desc_var, deadline = deadline_var)
    to_do_database.save()
    return redirect('todomain')

def deletetask(request):
    del_id = request.POST.get('id')
    del_2 = TodoDatabase.objects.get(id = del_id)
    del_2.delete()
    return redirect('todomain')

def deleteall(request):
    TodoDatabase.objects.all().delete()
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



# Create your views here.

