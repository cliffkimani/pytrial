from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login


#==================== General views here now

def home(request):
    return render_to_response("home.html")
    



#=================== Authentication views here now

def login(request):
    c = {}
    d = csrf(request)
    c.update(d)
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('accounts/invalid')


def loggedin(request):
    return render_to_response('loggedin.html',
                             {'full_name':request.user.username})
 
def invalid_login(request):
    return render_to_response('invalid_login.html')
    
def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')







    
