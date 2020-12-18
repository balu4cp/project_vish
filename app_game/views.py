from django.shortcuts import render
from app_game.models import *

# Create your views here.
import string   
import random    
import sys   
import traceback   
import json 
import os 
from django.shortcuts import render 
from django.http import HttpResponseRedirect 
from django.http import HttpResponse  
from django.contrib.auth import authenticate  
from django.contrib.auth import login    
from django.contrib.auth import logout  
from django.contrib.auth.decorators import login_required  
from django.views.decorators.http import require_GET     
from django.views.decorators.http import require_POST    
from django import db  
from django.db import transaction  
from django.contrib.auth.models import User  
from django.db.models import Q   
from django.core.exceptions import ValidationError
from datetime import datetime 
from django.conf import settings #Vishnupriya
from django.core.mail import EmailMessage#Vishnupriya
import random
# from app_alfred import utility
# from app_alfred.models import * 
def home(request):
    return render(request, 'home.html')


@require_GET
def user_list(request):
    try:
        print('************')
        friend_list = list(Friend.objects.all().values_list('user__id', flat=True))
        users = User.objects.filter(is_active=True).exclude(id__in=friend_list)
        user_list = []
        for user in users:
            user_dict = {
                'id':user.id,
                'name':user.username,
            }
            user_list.append(user_dict)
        print(user_list)
        return HttpResponse(content=json.dumps(user_list),content_type="application/json",status=200)
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        err = "\n".join(traceback.format_exception(*sys.exc_info()))
        print(err)
        return HttpResponse(content=json.dumps(err), content_type="application/json", status=406)


## Function to create a role.
# Author Jose
@require_POST
# @login_required
def api_create_role(request):
    try:
        print('======',request.POST)
        with transaction.atomic():            
            user_id = request.POST.get('user_id')
            code = request.POST.get('code')
            print(user_id,code)
            if not Code.objects.filter(user__id=user_id,code=code).exists():
                return HttpResponse(content=json.dumps('Invalid code'), status=406, content_type="application/json")
            current_user_id  = user_id
            user_id_list=list(User.objects.all().exclude(id=user_id).values_list('id', flat=True))
            # if current_user_id in user_id_list:
            #     user_id_list.remove(current_user_id)
            friend_list = list(Friend.objects.all().values_list('friend__id', flat=True))
            for i in friend_list:
                if i in user_id_list:
                    user_id_list.remove(i)
            secret =  random.choice(user_id_list)

            friend= Friend(user_id=current_user_id,
                            friend_id=secret)
            friend.full_clean()
            friend.save()
            msg =friend.friend.username


                


        return HttpResponse(content=json.dumps(msg), status=200, content_type="application/json")
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        err = "\n".join(traceback.format_exception(*sys.exc_info()))
        print(err)
        return HttpResponse(content=json.dumps(err), status=406, content_type="application/json")
