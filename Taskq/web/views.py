from django.shortcuts import render
from rest_framework.response import Response
from .models import TaskModel 
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from .forms import TaskForm 



def dashboard(request):
	"""	
    description:-->This function is used to reach homepage.
    author:--> Vikky Kumar
    returns:-->render
    Method_allowed:-->GET   
    
    """

	data=TaskForm()
	return render(request,'navbar.html',{"task_create_form":data})




def create_task(request):
    """
    description:-->This function is used to create task
    author:--> Vikky Kumar
    returns:-->redirect
    Method_allowed:-->POST
    
    """
    if request.method == 'POST':
    	obj=TaskForm(request.POST)
    	obj.save()
    return HttpResponseRedirect('/dashboard')



def sign(request):
    """
    description:-->This function is used to reach signup_page.
    author:--> Vikky Kumar
    returns:-->render
    Method_allowed:-->GET

    """
    return render(request,'signup.html')




def signup(request):
    """
    description:-->This function is used to create signup account.
    author:--> Vikky Kumar
    returns:-->redirect
    Method_allowed:-->POST

    """
    if request.method == 'POST':
    	username=request.POST['Username']
    	email=request.POST['email']
    	password=request.POST['password']
    	try:
    		print(username,password,email)
    		User.objects.create_user(username,email,password)
    		print("succesfully")
    		return HttpResponseRedirect('/log')
    	except Exception as e:
    		print("username already exit")
    		return HttpResponseRedirect('/sign')




def log(request):
    """
    description:-->This function is used to reach login_page.
    author:--> Vikky Kumar
    returns:-->redirect
    Method_allowed:-->GET

    """
    return render(request,'login.html')



@csrf_exempt
def login(request):
    """
    description:-->This function is used to login the user.
    author:--> Vikky Kumar
    returns:-->redirect
    Method_allowed:-->POST

    """
    if request.method == 'POST':
    	print(request.POST)
    	username=request.POST['username']
    	password=request.POST['password']
    	obj=authenticate(username=username,password=password)
    	if obj is not None:
    		print("User Acoount Exit")	
    		return HttpResponseRedirect('/dashboard')	
    	else:
    		print("user account doesn't exit")
    	return HttpResponseRedirect('/log')




def list_task(request):
	obj=TaskModel.objects.all()
	return render(request,'tasklist.html',{"task_list":obj})



def delete_task(request):
    obj=TaskModel.objects.get(id=request.GET['id'])
    obj.delete()
    messages.success(request,('item has been deleted'))
    return redirect ('/list_task')

def done_task(request,list_id):
    obj=TaskModel.objects.get(pk=list_id)
    item.completed=True
    item.save()
    return redirect ('/list_task')

