from django.shortcuts import render,redirect
from django.contrib import messages
from app.models import *
from django.core.paginator import Paginator


def showIndex(request):
    #result = ProductModel.objects.all()
    #return render(request,"index.html",{"data":result})

    result = ProductModel.objects.all()
    pa = Paginator(result,4)
    page_no = request.GET.get("page_no",1)
    page = pa.page(page_no)
    print(page.object_list)
#    return render(request, "index.html", {"page": page})
    cv = len(request.COOKIES)
    if cv == 0:
        return render(request, "index.html", {"data": ProductModel.objects.all(), "cvalue": cv,"page":page})
    else:
        return render(request, "index.html", {"data": ProductModel.objects.all(), "cvalue": cv-1,"page":page})


def admin_login(request):
    return render(request,"admin_login.html")


def admin_login_check(request):
    un = request.POST.get("t1")
    pa = request.POST.get("t2")

    if un == "bikram" and pa == "sahani":
        return redirect('admin_home')
    else:
        messages.error(request,"Invalid User")
        return redirect('admin_login')


def admin_home(request):
    return render(request,"admin_home.html")


def admin_view_users(request):
    return render(request,"admin_view_users.html",{"data":UserModel.objects.all()})


def admin_view_products(request):
    #result = ProductModel.objects.all()
    #return render(request,"admin_view_products.html",{"data":result})

    result = ProductModel.objects.all()
    pa = Paginator(result,2)
    page_number = request.GET.get("page_no",1)
    page = pa.page(page_number)
    return render(request,"admin_view_products.html",{"page":page})



def save_product(request):
    na = request.POST.get("p1")
    pr = request.POST.get("p2")
    qty = request.POST.get("p3")
    img = request.FILES["p4"]
    status = "active"
    ProductModel(name=na,price=pr,quantity=qty,photo=img,status=status).save()
    return redirect('admin_view_products')


def add_to_cart(request):
    k = request.GET.get("c1")
    v = request.GET.get("c2")
    response = redirect('main')
    response.set_cookie(k,v)
    return response


def in_cart(request):
#    return render(request,"in_cart.html",{"data":request.COOKIES})
    r = []
    for k, v in request.COOKIES.items():
        if k == "csrftoken" or k== "sessionid":
            continue
        else:
            w = ProductModel.objects.get(no=k)
            r.append(w)
    return render(request, 'in_cart.html', {'data': r})


def user_login(request):
    return render(request,"user_login.html")


def user_login_check(request):
    cno = request.POST.get("t1")
    pa = request.POST.get("t2")
    try:
        result=UserModel.objects.get(contact=cno, password=pa)
        request.session["user"] =result.no
        return render(request, "user_home.html", {"data": result})
    except UserModel.DoesNotExist:
        return render(request, "user_login.html", {"error": "Invalid user"})


def save_user(request):
    un=request.POST.get("c1")
    cno = request.POST.get("c2")
    email = request.POST.get("c3")
    pa = request.POST.get("c4")
    img = request.FILES["c5"]
    UserModel(name=un,contact=cno,email=email,password=pa,photo=img).save()
    return render(request,"user_login.html",{"success":"User Successfully Registered"})


def user_home(request):
    return render(request,"user_home.html")

def user_products(request):
    result = ProductModel.objects.all()
    pa = Paginator(result, 4)
    page_no = request.GET.get("page_no", 1)
    page = pa.page(page_no)
    print(page.object_list)
    #    return render(request, "index.html", {"page": page})
    cv = len(request.COOKIES)
    if cv == 0:
        return render(request, "user_products.html", {"data": ProductModel.objects.all(), "cvalue": cv, "page": page})
    else:
        return render(request, "user_products.html", {"data": ProductModel.objects.all(), "cvalue": cv - 1, "page": page})

def uadd_to_cart(request):
    k = request.GET.get("c1")
    v = request.GET.get("c2")
    response = redirect('user_products')
    response.set_cookie(k,v)
    return response

def delete_cart(request):
    response=redirect("user_products")
#    no = request.POST.get("no")
    for cookie in request.COOKIES:
        if cookie == "csrftoken":
            continue
        if cookie!= "csrftoken":
            response.delete_cookie(cookie)
    return response


