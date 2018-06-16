from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from webapp.models import *
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect,Http404,HttpResponse, JsonResponse
from django.template import RequestContext
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.decorators import login_required
# Create your views here.
@csrf_exempt
def login_main(request):

	context = RequestContext(request)

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		print(username,'lololo')
		user = authenticate(username=username, password=password)
		print(user)
		if user:
			if user.is_active:
				login(request, user)
				return JsonResponse({'status':'done','slug':user.username})
			else:
				return JsonResponse({'status':'fail','error_heading' : 'Account Inactive', 'error_message' :  'Your account is currently INACTIVE'})
		else:
			return JsonResponse({'status':'fail', 'error_heading' : 'Invalid Login Credentials', 'error_message' :  'Please try again'})
	else:
		error = 'POST request not sent'
		return render(request, 'login.html',{'error':error})

def user_logout(request):
    logout(request)
    return redirect('../../login/')

@csrf_exempt
@login_required
def dashboard(request, username):
    if request.user:
        self_user = request.user
        self_username = self_user.username
        username = str(username)
        if username == self_username:
            user_profile = Profile.objects.get(pk=self_user)
            # news_feed = Action.objects.all()
            context = {
                'user_profile' : user_profile,
                'user' : self_user,
                # 'news_feed':news_feed,
            }
            return render(request, 'self_dashboard.html', context)   

        else:
            profile_user = User.objects.get(username=username)
            user_profile = Profile.objects.get(user=profile_user)
            context = {
                'user' : self_user,
                'user_profile' : user_profile,
                'profile_user' : profile_user,
            }
            return render(request, 'profile_dashboard.html', context)
    else:
        pass

@csrf_exempt
def registration(request):

    context = RequestContext(request)
    
    registered = False
    
    if request.method == 'POST':
        username = request.POST['username']
        email =  request.POST['email']
        password = request.POST['password']
        # print(username,'pie')
        user = User()
        # password= user.password
        user.username = username
        user.set_password(password)
        user.email = email
        user.is_active = True
        user.save()
        # uid = user.id
        # body = "Thank You for Registering. Please Confirm your email:http://filmboard.ml/email_verify/"+ str(uid)+"/"
        # user_ob = user
        user = authenticate(username=username, password=password)
        # send_simple_message(user.email,body)
        login(request, user)
        profile = Profile()
        profile.user = user
        # profile.email_id  = email
        profile.save()
        return JsonResponse({'status':'done','slug':user.username})