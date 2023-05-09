from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDoList,Item
from .forms import  CreateNewList
from django import forms
from django.contrib import messages

# Create your views here.
def index(response, id):
    try:
        obj = ToDoList.objects.get(pk=id)
    except:
        obj = None
        return redirect('/create')
    if obj in response.user.todolist.all():
        if response.method =="POST":
            print(response.POST)
            if response.POST.get("save"):
                for item in obj.items.all():
                    if response.POST.get("c"+str(item.id)) == 'checked':
                        item.complete = True
                    
                    else:
                        item.complete = False 
                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")
                if len(txt)>1 :
                    obj.items.create(text = txt, complete = False)
                
            elif response.POST.get("deleteItems"):
                for item in obj.items.all():
                    if response.POST.get("c"+str(item.id)) == 'checked':
                        item.delete()

            elif response.POST.get('search-button'):
                all=ToDoList.objects
                if all.filter(name__exact=response.POST.get('searchbox')):
                    todo=ToDoList.objects.get(name=response.POST.get('searchbox'))
                    todo_id = todo.id
                    return redirect(f'/{todo_id}/')
                else:
                    input = response.POST.get('searchbox')
                    messages.warning(response, f'Sorry, you do not have a todo with the name "{input}"')
    
        context = {"obj":obj}
        return render(response, "main/items.html", context) 


    else:return redirect('/list')


    


def home(request):
    if request.POST.get('search-button'):
        all=ToDoList.objects
        if all.filter(name__exact=request.POST.get('searchbox')):
            todo=ToDoList.objects.get(name=request.POST.get('searchbox'))
            todo_id = todo.id
            return redirect(f'/{todo_id}/')
        else:
            input = request.POST.get('searchbox')
            messages.warning(request, f'Sorry, you do not have a todo with the name "{input}"')
            
    return render(request, "main/home.html" )





def create(response):
    form = CreateNewList()
    if response.method=="POST":
        form = CreateNewList(response.POST or None)
        
        if form.is_valid():
            if ToDoList.objects.filter(name__exact=form.cleaned_data['name']):
                input = form.cleaned_data['name']
                messages.warning(response, f'A todo with the name "{input}" already exists!')
            else:
                n = form.cleaned_data["name"]
                t= ToDoList(name=n)
                t.save()
                response.user.todolist.add(t)
                return redirect(f"/{t.id}/")
        elif response.POST.get('search-button'):
            all=ToDoList.objects
            if all.filter(name__exact=response.POST.get('searchbox')):
                todo=ToDoList.objects.get(name=response.POST.get('searchbox'))
                todo_id = todo.id
                return redirect(f'/{todo_id}/')
            else:
                input = response.POST.get('searchbox')
                messages.warning(response, f'Sorry, you do not have a todo with the name "{input}"')
     

    context = {"form":form, }
    return render(response, "main/create.html", context)





def list(response):
    if response.POST.get('search-button'):
        all=ToDoList.objects
        if all.filter(name__exact=response.POST.get('searchbox')):
            todo=ToDoList.objects.get(name=response.POST.get('searchbox'))
            todo_id = todo.id
            return redirect(f'/{todo_id}/')
        else:
            input = response.POST.get('searchbox')
            messages.warning(response, f'Sorry, you do not have a todo with the name "{input}", all available todos are listed below')
    return render(response, "main/list.html")





def delete(response):
    if response.method=='POST':
        if response.POST.get('del_btn'):
            for todo in response.user.todolist.all():
                if response.POST.get("c"+str(todo.id)) == 'checked':
                    todo.delete()
            return redirect("/list")
        elif response.POST.get('search-button'):
            all=ToDoList.objects
            if all.filter(name__exact=response.POST.get('searchbox')):
                todo=ToDoList.objects.get(name=response.POST.get('searchbox'))
                todo_id = todo.id
                return redirect(f'/{todo_id}/')
            else:
                input = response.POST.get('searchbox')
                messages.warning(response, f'Sorry, you do not have a todo with the name "{input}", all available todos are listed below')
    context= {}
    return render(response, 'main/del_todo.html',context)





def logout(response):
    context={}
    return render(response, "main/logout.html", context)