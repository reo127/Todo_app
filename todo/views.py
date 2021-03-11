from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from todo.models import MainTodo
from django.utils import timezone
from django.contrib import messages
# from django.contrib.humanize.templatetags import humanize



# Create your views here.


def todo(request):

    if request.method == "POST":
        time = timezone.now()
        sub = request.POST.get('sub')
        main = request.POST.get('main')
        print(sub)
        print(main)
        MainTodo.objects.create(time=time, subject=sub, contant=main)
        messages.success(request, 'Your work has been added in list')

    # If i teke this code in if then i got a error
    # I hava to give a defult valu if i want to avoid the error
    todoitems = MainTodo.objects.all().order_by('-time')
    param = {'todoitems':todoitems}


    return render(request, 'todo/todo.html', param)


def delete_todo(request, todo_sno):
    # MainTodo.objects.filter(id=todo_sno).delete()
    # MainTodo.objects.filter(todo_sno=sno)
    todo_obj = MainTodo(sno=todo_sno)
    todo_obj.delete()
    messages.success(request, 'Your work has been deleted')
    
    return HttpResponseRedirect('http://127.0.0.1:8000/todo/')
    # return render(request, 'todo/todo.html')

