import os
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CreateUserForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from .models import PostInfo
from django.http import HttpResponse



@login_required(login_url='login')
def home(request):
    return render(request, 'home/home.html')

@login_required(login_url='login')
def cdc(request):
    return render(request, 'home/cdc.html')


def loginPage(request):
    
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        context = {'username': username}

        if user is not None:
            login(request, user)
            if user.is_superuser:
                print("Superuser!!!!!!")
                return redirect('cdc')
            # return render(request, 'home/home.html', context)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    return render(request, 'home/login.html')


def registerPage(request):
    
    if request.user.is_authenticated:
        return redirect('home')

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Account created successfully")
            return redirect('login')

    context = {'form': form}
    return render(request, 'home/signup.html', context)

def logoutUser(request):
    """
    This view function is responsible for logging out the user and redirecting to the login page.
    """
    logout(request)
    return redirect('login')




def DataAdder(request):

    if request.method == 'POST':

        # resume file
        resume = request.FILES['resume_file']
        profile = request.FILES['profile']


        # Store Personal Details
        title=request.POST.get('topic')
        description=request.POST.get('description')
        explain=request.POST.get('explanation')
        average_investment=request.POST.get('average_investment')
        domain=request.POST.get('Domain')

        details = PostInfo.objects.create(
                user=User.objects.get(username=request.user.username),
                title=title,
                description=description,
                explain=explain,    
                image=profile,
                average_investment=average_investment,
                domain=domain,
                investment_file=resume
            )
            
        details.save()

        context = {
            'data_added': True
        }
        return render(request, 'home/home.html', context)
    return render(request, 'home/user.html')

def DataViewer(request):
    if request.method == 'GET':
        data = PostInfo.objects.all()
        return render(request, 'home/viewer.html', {'data': data})
    
    

def FullPost(request, title):
    data = get_object_or_404(PostInfo, title=title)
    return render(request, 'home/full.html', {'data': data})

def profile(request):
    if request.method=='GET':
        data=get_object_or_404(User)
        return render(request,'home/profile.html',{'data':data})
    
def invest_now_view(request,user):
    # Retrieve the email address from your SQLite database (replace with your own logic)
    info = get_object_or_404(User, username=user)
    # Render a template or redirect to a success page
    return render(request, "full.html",{'info':info})
