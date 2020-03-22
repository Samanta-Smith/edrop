from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
import random
from django.http import HttpResponse,JsonResponse
from django.conf.urls import url
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.contrib.auth import logout


def case(request,name):
    data = {"name": name,
            "object": Case.objects.get(name=name)
            }
    return render(request,'case.html',data)

def hello(request,name,case):
         userr =User.objects.get(username=name)
         profile = Profile.objects.get(user=userr)
         case= Case.objects.get(name=case)
         profile.save()
         news = Items()

         news.owner = profile
         num = random.randint(60, 65)
         if profile.bio>= case.price:
             profile.bio -= case.price
             profile.save()
             if case.name == "rare":
                           if num == 60:
                                  news.name = "Inscribed Snows of Frostivus"
                           elif num== 61:
                                  news.name=  "Heroic Deep Warden's Prized Scimitar"
                           elif num == 62:
                                  news.name= "Inscribed Humble Drifter"
                           elif num == 63:
                                  news.name= "Spying Toadstool"
                           elif num ==64:
                                  news.name= "Duskie"
                           elif num== 65:
                                  news.name= "Corrupted Jujak the Fiery Rebirth"
             elif case.name == "mythical":
                           if num == 60:
                                  news.name = "Timberthaw"
                           elif num== 61:
                                  news.name= "Genuine Shadow Flame"
                           elif num == 62:
                                  news.name= "The Serakund Tyrant"
                           elif num == 63:
                                  news.name= "Ethereal: Crystal Rift"
                           elif num ==64:
                                  news.name= "Inscribed Lil' Nova"
                           elif num== 65:
                                  news.name= "Infused Shield of the Silent Edict"
             elif case.name =="legendary":
                           if num == 60:
                                  news.name = "Bindings of Deep Magma"
                           elif num== 61:
                                  news.name=  "International 2018 Autograph: Saahil"
                           elif num == 62:
                                  news.name= "Baby Roshan"
                           elif num == 63:
                                  news.name= "Bestowments of the Divine"
                           elif num ==64:
                                  news.name= "Inscribed Battlefury"
                           elif num== 65:
                                  news.name= "Unusual Butch"
             elif case.name =="arcane":
                           if num == 60:
                                  news.name = "Exalted Swine of the Sunken Galley"
                           elif num== 61:
                                  news.name=  "Tempest Helm of the Thundergod"
                           elif num == 62:
                                  news.name= "Exalted Manifold Paradox"
                           elif num == 63:
                                  news.name= "Exalted Blades of Voth Domosh"
                           elif num ==64:
                                  news.name= "Exalted Frost Avalanche Bundle"
                           elif num== 65:
                                  news.name= "Exalted Fractal Horns of Inner Abysm"

             news.save()
             return HttpResponse(num)

def index(request):
    if request.user.is_authenticated:
     data = {
            "objects": Case.objects.all(),
            "items": Items.objects.filter(owner=request.user.profile),
            }
    else:
      data = {
            "objects": Case.objects.all(),
             }
    return render(request,'index.html',data)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
