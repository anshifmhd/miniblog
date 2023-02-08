from django.shortcuts import render, redirect
from user.models import User, Account, Blog, Comments

# Create your views here.


def index(request):
    object = Blog.objects.all()
    obj = Account.objects.get(user_id = request.session['userid'])
    return render(request,'index.html',{'data':obj, 'objects':object})



def login(request):
    msg = ""
    if request.method =="POST":
        if 'u_register' in request.POST:
            name = request.POST['Name']
            email = request.POST['Email']
            password = request.POST['Password']
            username = request.POST['Username']
            username_exist = Account.objects.filter(username = username).exists()
            if not username_exist:
                obj = User(name = name, email = email)
                obj.save()
                account = Account(username = username, password = password, type = 'user', user_id = obj.id )
                account.save()
            else:
                msg = 'username already exist'

        if 'u_login' in request.POST:
            login_username = request.POST['username']
            login_password = request.POST['password']
            try:
                object = Account.objects.get(username = login_username, password = login_password)
                request.session['userid'] = object.id
                return redirect('user:index')
            except:
                return render(request,'login.html',{'message':'invalid username or password'})

    return render(request,'login.html',{'error_msg':msg})


def logout(request):
    del request.session['userid']
    return redirect('user:login')


def add_blog(request):
    if request.method == "POST":
        title = request.POST['title']
        subtitle = request.POST['subtitle']
        description = request.POST['description']
        image = request.FILES['image']

        obj = Blog(title = title, subtitle = subtitle, description = description, image = image, user_id = request.session['userid'])
        obj.save()

    return render(request,'add_blog.html')



def edit_profile(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']

        obj = Account.objects.get(id = request.session['userid'])
        User.objects.filter(id = obj.user_id).update(name = name, email = email)
        # Account.objects.filter(id = request.session['userid']).update(username = username)
        username_exist = Account.objects.filter(username = username).exists()
        if not username_exist:
            Account.objects.filter(id = request.session['userid']).update(username = username)

        else:
            msg = 'username already exist'


    obj = Account.objects.get(user_id = request.session['userid'])
    return render(request,'edit_profile.html',{'data':obj})




def change_password(request):
    message = ""
    msg = ""
    mess = ""
    if request.method == "POST":
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        obj = Account.objects.get(id = request.session['userid'])
        if obj.password == current_password:
            if new_password == confirm_password:
                Account.objects.filter(id = request.session['userid']).update(password = confirm_password)
                mess = "Your password changed successfully"
            else:
                message = 'please confirm new password'
        else:
            msg = 'enter your correct password'
    return render(request,'change_password.html',{'msg':msg, 'message':message, 'mess':mess})



def comment(request,idd):
    print(idd)
    oo = Blog.objects.get(id = idd)
    print(oo)
    if request.method == "POST":
        oo = Blog.objects.get(id = idd)
        comment = request.POST['comment']
        object = Comments(comments = comment, user_id = request.session['userid'], blog_id = oo.id)
        print(object)
        object.save()
        return redirect('user:index')
    return render(request,'comment.html')




def view_comment(request,idd):
    o = Blog.objects.get(id = idd)
    obj = Comments.objects.filter(blog_id = o.id)

    return render(request,'view_comment.html',{'data':o,'d':obj})