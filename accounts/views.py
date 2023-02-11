from django.shortcuts import render, redirect

def register(request):
    # helps to validate the request
    if request.method == 'POST':
        print('Form Submitted')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    # helps to validate the request
    if request.method == 'POST':
        print('Form Submitted')
        return redirect('register')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

