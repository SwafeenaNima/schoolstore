from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from schoolstore_app.models import Department, Course, Order
from .forms import OrderForm



def home(request):
    return render(request, 'home.html')

def login(request):
    error_message = None
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                #login(request, user)
                return redirect('new_page')  # Redirect to the new page after successful login
        else:
            error_message = "Invalid username or password. Please try again."
    else:
        form = AuthenticationForm()
        print(error_message)
    return render(request, 'login.html', {'form': form, 'error_message': error_message})

def user_logout(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        # Get the form data
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if the passwords match
        if password != confirm_password:
            error_message = "Passwords do not match. Please try again."
            return render(request, 'register.html', {'error_message': error_message})

        if User.objects.filter(username=username).exists():
            error_message = "Username is already taken. Please choose a different username."
            return render(request, 'register.html', {'error_message': error_message})

        #user = User.objects.create_user(username=username, password=password)

        #login(request, user)

        return redirect('login')

    return render(request, 'register.html')


def new_page(request):

    departments_list = Department.objects.all()
    return render(request, 'new_page.html', {'departments_list': departments_list})

def submit_order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        department_id = request.POST.get('department')
        course = request.POST.get('course')
        purpose = request.POST.get('purpose')
        materials = request.POST.getlist('materials')
        if(materials==''):
            materials=''
        Order.objects.create(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone=phone,
            email=email,
            address=address,
            department_id=department_id,
            course=course,
            purpose=purpose,
            materials=materials,
        )
        return render(request, 'success.html')
    else:
        return redirect('new_page', {'error_message': 'Please Fill The form Correctly'})


def get_courses_for_department(request, department_id):
    try:
        courses = Course.objects.filter(department_id=department_id).values_list('name', flat=True)
        courses = list(courses)
        return JsonResponse({"courses": courses})
    except Department.DoesNotExist:
        return JsonResponse({"courses": []})



