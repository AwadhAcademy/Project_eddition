from django.shortcuts import render
from .models import Carousel_Data
from .models import loogin_data
from .models import project_details
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate 
# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('name')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(
                request, f"You are now logged in as {username}.")
                return redirect(request, "home/home.html")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "home/home.html")
def about(request):
    photo = Carousel_Data.objects.all()
    n = len(photo)
    params = {'photo':photo}
    return render(request, "home/about_us.html",params)
def sign_in(request):
    if request.method =='POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        phone = request.POST.get('phone')
        if password1 ==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already registred")
                return render(request, "home/sign_in.html")
            else:
                data = loogin_data(name=name,last_name=last_name,password1=password1,password2=password2,phone=phone,email=email)
                # print(name)
                data.save()
                params = {"name":name}
                return render(request, "home/user_planer.html",params)
        else:
            messages.info(request, "Password Does Not Mathch")
            return render(request, "home/sign_in.html")
    return render(request, "home/sign_in.html")
def user_planer(request):
    name = request.POST.get('name')
    params = {'name':name}
    return render(request, "home/user_planer.html",params)
def project(request):
    details = project_details.objects.all()
    params = {'details':details}
    return render(request, "home/project.html",params)
