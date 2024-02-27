from django.shortcuts import render, redirect
from Blog.models import Members

# Create your views here.
def home(request):
    return render(request, 'index.html')
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