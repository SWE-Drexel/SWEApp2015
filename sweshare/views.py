from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required

#Authentication and registration
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/goalpage/')
	
@login_required
def restricted(request):
    if not request.user.is_authenticated():
        return HttpResponse("You are logged in.")
    else:
        return HttpResponse("You are not logged in.")
	
def login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                return HttpResponse("Your account is disabled. Please contact an administrator.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid username or password.")
    else:
        return render_to_response('loginpage.html', {}, context)

def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
			
        else:
			error = True
			print user_form.errors
    else:
        user_form = UserForm()
    return render_to_response('register.html',{'user_form': user_form, 'registered': registered},context_instance=RequestContext(request))

#Page rendering functions
def admin(request):
    return render_to_response('admin.html',{},context_instance=RequestContext(request))

def home(request):
    return render_to_response('home.html',{},context_instance=RequestContext(request))

def register(request):
    return render_to_response('register.html',{},context_instance=RequestContext(request))

def loginpage(request):
	return render_to_response('loginpage.html',{},context_instance=RequestContext(request))

def goalpage(request):
    return render_to_response('goalpage.html',{},context_instance=RequestContext(request))

# Action functions
