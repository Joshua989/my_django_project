
from django.shortcuts import render
from .models import Task # Import the Task model from the current application

def task_list(request):
    tasks = Task.objects.all() # Retrieve all Task objects from the database
    context = {'tasks': tasks} # Create a context dictionary with the retrieved tasks
    return render(request, 'tasks/task_list.html', context) # Render the 'task_list.html' template with the context data

