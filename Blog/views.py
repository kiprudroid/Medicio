import json
from django.shortcuts import render, redirect
from mechanize import HTTPBasicAuthHandler
import requests
from Blog.credentials import LipanaMpesaPpassword, MpesaAccessToken
from Blog.models import Members,Response, Users ,ImageModel
from Project.forms import ImageUploadForm
from django.http import HttpResponse

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

def token(request):
    consumer_key = 'ePeSz5tnbI0k3fhj6AFiitFU5yAmRfDIPO16nBSPsIrSy5dH'
    consumer_secret = 'QNm2CQsgyYqZAsu0DUja6G3vNyTTdGHd0jYG11F9QoEsEJeCDenJePLSEI1eTE8j'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuthHandler(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')



def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Apen Softwares",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse(response)

