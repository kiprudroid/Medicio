from django.shortcuts import render, redirect
from Blog.models import Members,Response, Users ,ImageModel
from Project.forms import ImageUploadForm

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
        return redirect('/login')
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

def adminhome(request):
    if request.method =="POST":
        if Members.objects.filter(username=request.POST['username'],
                                 password = request.POST['password']).exists():
                member = Members.objects.get(username=request.POST['username'],
                                             password = request.POST['password'])
                return render(request,'adminhome.html',{'member' : member})
        else:
             return render(request,'login.html',{'error' : 'Invalid username or password'})
    else:
        return render(request,'login.html')
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'showimage.html', {'images': images})

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')