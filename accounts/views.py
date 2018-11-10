from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contact

# Create your views here.
def register(request):
    if request.method == 'POST':
        #get form values
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        #Password check
        if password == password2:
            #Check user name
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username alrady exist')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                   messages.error(request,'Email alrady exist')
                   return redirect('register')
                else:
                    #looks good, So register user 
                    user = User.objects.create_user(
                        username=username,
                        first_name = first_name,
                        last_name = last_name,
                        email = email,
                        password = password,)
                    #login After successfully register
                    '''auth.login(request,user)
                    messages.success(request,'Registered successfully')
                    return  redirect('/')'''
                    user.save()
                    messages.success(request,'You are now Registered successfully you can login your account')
                    return redirect('login')
                         
        else:
            messages.error(request,'Password do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
     if request.method == 'POST':
        #login Logic
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password,)
        
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are logged In')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')
        
     else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are logged out now')
        return redirect('index')


def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id = request.user.id)
    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html',context)