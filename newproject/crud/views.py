from django.shortcuts import render,redirect, get_object_or_404
from .models import Student
from django.db.models import Q



def home(request):
    query = request.GET.get('q')

    if query:
        crud = Student.objects.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(roll__icontains=query) |
            Q(phone__icontains=query)
        )
    else:
        crud = Student.objects.all()

    return render(request, 'crud/home.html', {'crud': crud})


def crud_add(request):
    if request.method=='POST':
        roll = request.POST.get('crud_roll')
        name = request.POST.get('crud_name')
        email = request.POST.get('crud_email')
        address = request.POST.get('crud_address')
        phone = request.POST.get('crud_phone')
        # create an object for models
        s=Student()
        s.roll=roll
        s.name=name
        s.email=email
        s.address=address
        s.phone=phone
        s.save()
        
        return redirect("/crud/home/")
    return render(request,"crud/add_crud.html",{})

def crud_delete(request,roll):
    s=Student.objects.get(pk=roll)
    s.delete()
    
    return redirect('/crud/home')

def crud_update(request, roll):
    student = get_object_or_404(Student, roll=roll)
    student 
    return render(request, 'crud/update_crud.html', {
        'student': student
    })


def docrud_update(request, roll):
    if request.method != "POST":
        return redirect('home')

    student = get_object_or_404(Student, roll=roll)

    student.name = request.POST.get('crud_name', student.name)
    student.email = request.POST.get('crud_email', student.email)
    student.address = request.POST.get('crud_address', student.address)
    student.phone = request.POST.get('crud_phone', student.phone)

    student.save()

    return redirect('home')
