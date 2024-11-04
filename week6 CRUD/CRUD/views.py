from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import user_passes_test
from .models import Student
from django.contrib.auth import logout



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cnpassword=request.POST['cpassword']

        if password==cnpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'this user name is already exists!!!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.info(request,'user created successfully')
        else:
            messages.info(request,'password does not match !!!')    
            return redirect('register')           
    return render(request, 'register.html')  
# csrf  external import method
@csrf_exempt
# cache clear
@never_cache

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(username=username, password=password)
        if user is not None:
            # Authentication successful
            request.session["uid"] = user.id
            login(request, user)

            # Check user role and redirect based on role
            if user.is_superuser:
                return redirect('admin_home')  # Redirect to admin home page
            else:
                return redirect('home')  # Redirect to regular user's home page
        else:
            messages.error(request, 'Invalid username or password!')
            return render(request, 'login.html')
    return render(request, 'login.html')  

@never_cache
@login_required(login_url='user_login')
def home(request):
     username = request.user.username
     return render(request, 'home.html', {'username': username})


# Custom decorator to check if the user is an admin
def admin_required(user):
    return user.is_superuser

@user_passes_test(admin_required)  # Only admin (superuser) can access this view
def admin_home(request):
    search_query = request.GET.get('search', '')
    if search_query:
        # Simple filter by a single field
        students = Student.objects.filter(firstname__icontains=search_query)
    else:
        students = Student.objects.all()  # Return all students if no search query

    return render(request, 'admin_home.html', {'students': students, 'search_query': search_query})
        
# Add student page load
def add(request):
    return render(request,'add.html')

# Add student records
def addrecords(request):
    if request.method == 'POST':
        firstname = request.POST.get('first')
        lastname = request.POST.get('second')
        subject = request.POST.get('subject')
        mark = request.POST.get('mark')
        image = request.FILES.get('image')  # Use request.FILES for file uploads
        new_student = Student(firstname=firstname, lastname=lastname, subject=subject, mark=mark, image=image)
                
        new_student.save()
        messages.success(request, "Student added successfully.")
        return redirect('admin_home')
    else: 
       return render(request, 'add.html')

# delete record from student details
def delete_record(request,record_id):
    record = Student.objects.get(id=record_id)
    record.delete()
    messages.success(request, "Student deleted successfully.")

    return redirect('admin_home')

# update records from student details
def update(request, student_id):

    student = Student.objects.get(id=student_id)
    return render(request, 'update.html', {'student': student})

def update_student(request, student_id):
    student =Student.objects.get(id=student_id)  
    if request.method == 'POST':
        # Retrieve and update student fields
        student.firstname = request.POST.get('firstname')
        student.lastname = request.POST.get('lastname')
        student.subject = request.POST.get('subject')
        student.mark = request.POST.get('mark')

        # Handle image upload
        if 'image' in request.FILES and request.FILES['image']:
            student.image = request.FILES['image']

        # Save the updated student object
        student.save()
        messages.success(request, "Student updated successfully.")

        return redirect("admin_home")  # Change this to a specific URL if needed

    return render(request, 'update.html', {'student': student})  # Render the form with the existing student data

def admin_logout(request):
    logout(request)  # Log out the user
    messages.success(request, "You have been logged out successfully.")
    return redirect('user_login')