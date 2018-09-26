from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate

def acc_login(request):
    error_msg = ''
    if request.method == "POST":
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect(request.GET.get('next','/crm/'))
        else:
            error_msg = "用户名或密码错误"
    return render(request,'login.html',{'error_msg':error_msg})

def acc_logout(request):
    logout(request)
    return redirect('/login/')