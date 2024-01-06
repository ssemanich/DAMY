from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

class newtaskForm(forms.Form):
    task=forms.CharField(label="New Task")
    priority=forms.IntegerField(label="priority", min_value=1,max_value=10)
# Create your views here.
def add(request):
    if request.method=="POST":
        form=newtaskForm(request.POST)
        if form.is_valid_():
           task=form.cleaned_data["task"]
           request.session["tasks"] +=[task]
           return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request,"tasks/add.html",{
                "form":form
            })
    return  render(request,"tasks/add.html",{
        "form":newtaskForm()
    })
    
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]
    return render(request, "tasks/index.html",{
        "tasks":request.session["tasks"]
    })
    