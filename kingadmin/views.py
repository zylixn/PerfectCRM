from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from kingadmin import app_setup
#程序已启动就自动执行
app_setup.kingadmin_auto_discover()
from kingadmin.sites import site

def app_index(request):
    return render(request,'kingadmin/app_index.html',{'site':site})

def acc_login(request):
    error_msg = ''
    if request.method == "POST":
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect(request.GET.get('next','/kingadmin/'))
        else:
            error_msg = "用户名或密码错误"
    return render(request,'kingadmin/login.html',{'error_msg':error_msg})

def acc_logout(request):
    logout(request)
    return redirect('/login/')

def get_filter_result(request,querysets):
    filter_conditions = {}
    for key,val in request.GET.items():
        if val:
            filter_conditions[key] = val
    return querysets.filter(**filter_conditions),filter_conditions

@login_required
def table_obj_list(request,app_name,model_name):
    """
    取出指定model里的数据返回给前端
    :param request:
    :param app_name:
    :param model_name:
    :return:
    """
    admin_class = site.enable_admins[app_name][model_name]
    querysets = admin_class.model.objects.all()
    querysets,filter_conditions = get_filter_result(request,querysets)
    admin_class.filter_conditions = filter_conditions
    return render(request,'kingadmin/table_obj_list.html',{'querysets':querysets,"admin_class":admin_class})