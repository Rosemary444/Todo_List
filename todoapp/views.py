from django.shortcuts import render,redirect
from todoapp.forms import todoform,editTask
from todoapp.models import Todo
# Create your views here.
def todolist(request):
  
  if request.method == 'POST':
    form=todoform(request.POST)
    if form.is_valid():
      print("validation success")
      print(form.cleaned_data['title'])
      form.save()
      return redirect('todolist')
  else:
      all_task=Todo.objects.all()
      form=todoform()
  return render(request,'index.html',{'forms':form ,'list':all_task})


def edit_task(request,id=0):
   data=Todo.objects.get(id=id)
  #  EditForm=editTask()
   if request.method == 'POST':
      EditForm=editTask(request.POST,instance=data)
      if EditForm.is_valid():
            EditForm.save()
            return redirect('todolist')
   else:
      EditForm=editTask(instance=data)

   return render(request,'edittask.html',{'edit':data,'editform':EditForm})

def deletetask(request,id=0):
   data=Todo.objects.get(id=id)
   data.delete()
   return redirect('todolist')