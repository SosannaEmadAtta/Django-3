from lib2to3.fixes.fix_input import context
from sys import exception
from .ModelForm import AccountForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import*
from django.shortcuts import get_object_or_404
from .models import Account


# Create your views here

def create_account(request):

    if request.method == 'POST':
        form = AccountForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
      
    else:
        form = AccountForm()
    return render(request, 'account/create_account.html', {'form': form})


def update_account(request, id):

    account = get_object_or_404(Account, pk=id)

    if request.method == 'POST':
        form = AccountForm(request.POST,request.FILES, instance=account)
        if form.is_valid():
            form.save()
            return redirect('account_detail', id=account.id)
    else:
        form = AccountForm(instance=account)
    return render(request,'account/update_account.html',{'form': form})

    



def delete_account(request, id):
    context = {}
    try:
        Account.objects.filter(pk=id).delete()
        context = {"id": id, 'msg': 'account is deleted'}


    except:
        import sys
        context['error'] = sys.exc_info()[1]
    return render(request, 'account/delete_account.html', context)



def login(request):
    context = {}
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                account = Account.objects.get(email=email, password=password)
                return redirect('account_detail', id=account.id)
            except Account.DoesNotExist:
                context['error'] = "Invalid email or password"
    else:
        form = AccountForm()
    context['form'] = form
    return render(request , 'account/account_login.html', context)

def list_account(request):
    context = {}
    accountsobj = Account.objects.all()
    context["accounts"] = accountsobj
    return render(request, "account/list_account.html", context)


def account_detail(request, id):
    account = get_object_or_404(Account, pk=id)
    return render(request, 'account/account_detail.html', {'account': account})
