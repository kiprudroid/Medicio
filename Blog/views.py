from django.shortcuts import render, redirect
from Blog.models import Members,Response, Users

# Create your views here.
def home(request):
    if request.method == 'POST':
        response = Response(fullname = request.POST['fullname'],email = request.POST['email'],subject = request.POST['subject'],message = request.POST['message'])
        response.save()
        return redirect('/')
    else:
       return render(request,'index.html')
    
    
def inner(request):
    return render(request, 'inner-page.html')
def register(request):
    if request.method == 'POST':
        members = Members(username = request.POST['username'],email = request.POST['email'],password = request.POST['password'])
        members.save()
        return redirect('/register')
    else:
       return render(request,'register.html')
    
def login(request):
    return render(request, 'login.html')
def upload(request):
    return render(request, 'upload.html')

def detail(request):
    details = Response.objects.all()
    return render(request,'details.html',{'details' : details})

def members(request):
    member = Users.objects.all()
    return render(request,'members.html',{'member' : member})