import datetime
from django.shortcuts import redirect, render
from . forms import CreateTaskForm
from . models import Task,Category

# Create your views here.
def home(request):
    categories=Category.objects.all()
    utilization=7.0
    for cat in categories:
        if cat.overhead>cat.alloted:
            cat.overhead-=cat.alloted
            secAlc = cat.alloted.seconds
            minAlc = secAlc // 60
            secOvh = cat.overhead.seconds
            minOvh = secOvh // 60
            if minAlc>0.0 and minOvh>0.0:
                hrAlc = minAlc // 60.0
                minAlc = minAlc % 60
                hrOvh = minOvh // 60.0
                minOvh = minOvh % 60
                utilization+=((hrOvh+(minOvh/60.0))/(hrAlc+(minAlc/60.0)))
    return render(request,'tasks/index.html',{"utilization":700.0/utilization})
def dashboard(request):
    categories=Category.objects.all()
    context={'categories':categories}
    return render(request,'tasks/dashboard.html',context=context)
def createTask(request):
    form=CreateTaskForm()
    if request.method == 'POST':
        form=CreateTaskForm(request.POST,initial={'timeStarted': (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=5,minutes=30))})
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form':form}
    return render(request,'tasks/create-task.html',context=context)
def viewTask(request):
    task=Task.objects.all()
    context={'task':task}
    return render(request,'tasks/view-task.html',context=context)
def updateTask(request,pk):
    task=Task.objects.get(id=pk)
    form=CreateTaskForm(instance=task)
    if request.method=='POST':
        form=CreateTaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form':form}
    return render(request,'tasks/update-task.html',context=context)
def completeTask(request, pk):
    task=Task.objects.get(id=pk)
    category=Category.objects.get(name=task.category)
    if request.method == 'POST':  
        task.timeCompleted=(datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=5,minutes=30))
        task.save()
        task.overhead=abs((task.timeCompleted-task.timeStarted)-task.timeAlloted)
        task.save()
        if (task.timeCompleted-task.timeStarted)>task.timeAlloted:
            category.overhead+=task.overhead
            category.save()
        else:
            category.overhead-=task.overhead
            category.save()
        return redirect('view-task')
    return render(request,'tasks/complete-task.html')