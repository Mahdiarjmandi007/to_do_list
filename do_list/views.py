import json
from django.shortcuts import render
from do_list.models import *
from django.utils import timezone
from django.http import JsonResponse
def create(request):
    if request.method=='POST':
        action=request.POST.get('action')
        if action=='create':
            data=request.POST
            title=data.get('title')
            description =data.get('description')
            do_list.objects.create(titles=title,descriptions=description)
            return JsonResponse({'message': 'Task created'})
def done (request):
    if request.method=='PATCH':
        data = json.loads(request.body)
        task_id = data.get('id')
        task = do_list.objects.get(id=task_id)
        task.statuss = True
        task.e_date = timezone.now()
        task.save()
        return JsonResponse({'message': 'Task completed'})
def delete(request):
    if request.method=='DELETE':
        data = json.loads(request.body)
        task_id = data.get('id')
        task=do_list.objects.get(id=task_id)
        task.delete()
        return JsonResponse({'message': 'Task deleted'})
def task (request):
    if request.method=='GET':
        task=do_list.objects.all()
        data=list(task.values())
        return JsonResponse(data, safe=False)


# Create your views here.
