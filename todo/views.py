from django.shortcuts import render,redirect,get_object_or_404
from todo.models import Todo
from todo.forms import TodoForms
from todo.forms import ContactForm
from todo.models import Contact
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'home.html')
@login_required
def about(request):
    return render(request,'about.html')
@login_required
def contact(request):
    contactform= ContactForm(request.POST or None)
    if contactform.is_valid():
        contactform.save()
        return redirect('home')
    return render(request,'contact.html',{'form':contactform})
@login_required
#add the feedbacks
def todoadd(request):
    todoform= TodoForms(request.POST or None)
    if todoform.is_valid():
        todoform.save()
        return redirect('todolist')
    return render(request,'todoadd.html',{'form':todoform})
@login_required
#reading all the feedbacks
def todolist(request):
    allfeedback= Todo.objects.all()
    return render(request,'todolist.html',{'todos':allfeedback})
@login_required
def todoedit(request,pk):
    todo=get_object_or_404(Todo,pk=pk)
    todoform =TodoForms(request.POST or None, instance=todo)
    if todoform.is_valid():
        todoform.save()
        return redirect('todolist')
    return render(request,'todoadd.html',{'form':todoform})
@login_required
def tododelete(request,pk):
    todo=get_object_or_404(Todo,pk=pk)
    if request.method=='POST':
        todo.delete()
        return redirect('todolist')
    return render(request,'tododelete.html',{'todo':todo})