from django.urls import reverse
from django.db.models import Count
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import formset_factory, modelformset_factory
from .models import *
from .models import TrainingValue
from .models import Training as TrainingModel
from .forms import *

# Create your views here.
def pakarKNN(request):
    return render(request, 'pakar/knn.html')

def index(request):
    return render(request, 'front/landing.html')

def dasbor(request):
    return render(request, 'front/dasbor.html')

def akun(request):
    return render(request, 'akun/index.html')

def editAkun(request):
    return render(request, 'akun/editakun.html')

# TRAINING #
def dataTraining(request):
    trainings = TrainingModel.objects.all()
    data = {'trainings': trainings}
    return render(request, 'training/index.html', data)

def createTraining(request):
    form = TrainingForm()
    if request.method == "POST":
        form = TrainingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('training'))
    data = {'form':form}
    return render(request, 'training/create.html', data)

def updateTraining(request, id):
    train = TrainingModel.objects.filter(pk=id).first()
    form = TrainingForm(instance=train)
    if not train:
        return redirect(reverse('create_training'))
    else:
        if request.method == "POST":
            form = TrainingForm(request.POST, instance=train)
            if form.is_valid():
                print(train.id)
                form.save()
                return redirect(reverse('training'))
    data = {'training':train,'form':form}
    return render(request, 'training/update.html', data)

def deleteTraining(request, id):
    train = TrainingModel.objects.filter(pk=id).first()
    if not train:
        return redirect(reverse('training'))
    else:
        train.delete()
    return redirect(reverse('training'))


# DATA TRAINING
def seeDataTraining(request, id):
    dtrain = TrainingValue.objects.filter(training_id=id)
    attr = Attribute.objects.all()
    data = {'dtrain':dtrain, 'attr':attr}
    return render(request, 'training/see_training.html', data)

def updateDataTraining(request, id):
    dtrain = TrainingValue.objects.filter(id=id).first()
    form = DataTrainingForm(instance=dtrain)
    if not dtrain:
        return redirect(reverse('training'))
    else:
        if request.method == "POST":
            form = DataTrainingForm(request.POST ,instance=dtrain)
            if form.is_valid():
                form.save()
                return redirect(reverse('training'))
    data = {'dtrain':dtrain, 'form':form}
    return render(request, 'training/update_training.html', data)

def createDataTraining(request, id):
    train = TrainingModel.objects.filter(pk=id).first()
    attr = Attribute.objects.all()
    amount_attr = attr.count()
    init_val = []
    for val in attr:
        init_val.append({
        'training_id': id,
        'attribute_id':val.id
        })
    DataTrainingFormSet = formset_factory(DataTrainingForm, extra=0)
    formset = DataTrainingFormSet(initial=init_val)
    # formset = modelformset_factory(TrainingValue, exclude=()) #update batch dari model
    if request.method == "POST":
        formset = DataTrainingFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                form.save()
            return redirect(reverse('training'))
    data = {'formset':formset}
    return render(request, 'training/create_training.html', data)

def createAttribute(request):
    return render(request, 'training/create_attribute.html')

# LAB #
def lab(request):
    labs = Lab.objects.all()
    data = {'labs': labs}
    return render(request, 'lab/index.html', data)

def createLab(request):
    form = LabForm()
    if request.method == "POST":
        form = LabForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('lab'))
    data = {'form':form}
    return render(request, 'lab/create.html', data)

def updateLab(request, id):
    # lab = Lab.objects.get(pk=id)
    lab = Lab.objects.filter(pk=id).first()
    form = LabForm(instance=lab)
    if not lab:
        return redirect(reverse('create_lab'))
    else:
        if request.method == "POST":
            form = LabForm(request.POST, instance=lab)
            if form.is_valid():
                print(lab.id)
                form.save()
                return redirect(reverse('lab'))
    data = {'lab':lab,'form':form}
    return render(request, 'lab/update.html', data)

def deleteLab(request, id):
    lab = Lab.objects.filter(pk=id).first()
    if not lab:
        return redirect(reverse('lab'))
    else:
        lab.delete()
    return redirect(reverse('lab'))
