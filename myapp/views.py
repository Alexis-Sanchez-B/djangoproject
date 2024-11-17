from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project,Task #consultar a la BD
from django.shortcuts import get_object_or_404 #Obtenemos para dar error 404 cuando no se encuentre un dato

# Create your views here.
def index(request):
    title = 'DJANGO COURSE!!'
    return render(request, 'index.html',{
        'title': title
    })

def about(request):
    username = 'asanchez'
    return render(request,'about.html',{
        'username': username
    })

#se concatena el username que se solicita
def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" %username)

def perro(request):
    return HttpResponse("Hola Perro")

def projects(request):
    #project = list(Project.objects.values()) #Esto devuelve un query set para mandar al cliente
    #return JsonResponse(project, safe=False)
    projects = Project.objects.all()
    return render(request, 'projects.html',{
        'projects': projects
    })

def tasks(request):
    #task = Task.objects.get(id=id) #Buscamos una tarea en la base de datos 
    #task = get_object_or_404(Task, id=id)
    #return HttpResponse('task: %s'% task.title)
    tasks = Task.objects.all()
    return render(request,'tasks.html',{
        'tasks': tasks
    })