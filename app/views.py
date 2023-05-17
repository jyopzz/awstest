
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login
from .form import LoginForm
from django.http import HttpResponse
from .models import Getnamemod,details
# Create your views here.



def loginn(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,
                              username=cd['username'],
                              password =cd['password'])
            
            if user is not None:
                login(request, user)
                return HttpResponse('Login Successfull')
            else:
                return HttpResponse('login failed')
    else :
        form=LoginForm()

    return render(request,'login.html',{'form':form})

def main(request):
   
    data={"details1":details.objects.all()}

    return render(request,'main.html',data)


def insertdata(request):
    if request.method=="POST":
        name=request.POST.get('name1')
        image=request.FILES['img']
        print(name,image)
        detailsobj=details()
        detailsobj.name=name
        detailsobj.image=image
        detailsobj.save()
    return redirect(main)

def edit(request,id):
    if request.method=="POST":
        name=request.POST.get('name1')
        image=request.FILES['img']
        
        detailsobj=details.objects.get(id=id)
        detailsobj.name=name
        detailsobj.image=image
        detailsobj.save()
        return redirect(main)



    data={"details1":details.objects.filter(id=id)}
    print(data)
    
    return render(request,'edit.html',data)



    


def delete(request,id):
    data=details.objects.get(id=id)
    data.delete()
    return redirect(main)