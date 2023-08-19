from django.shortcuts import render,redirect
from .models import List
# Create your views here.

def list(request):
    if request.method == "POST":
        title = request.POST["title"]
        task = List.objects.create(title=title)
        task.save()
        return redirect("list:list")
    active = List.objects.filter(completed=False)
    completed = List.objects.filter(completed=True)
    context = {
        "active":active,
        "completed":completed
    }
    return render(request,"to-do-list-4.html",context)

def done(request,slug):
    task = List.objects.get(slug=slug)
    done = List.objects.create(completed=True,title=task.title)
    done.save()
    task.delete()
    return redirect("list:list")

def undo(request,slug):
    task = List.objects.get(slug=slug)
    undo = List.objects.create(completed=False,title=task.title)
    undo.save()
    task.delete()
    return redirect("list:list")

def delete(request,slug):
    delete = List.objects.get(slug=slug)
    delete.delete()
    return redirect("list:list")
    


        

