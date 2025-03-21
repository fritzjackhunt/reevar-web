from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'reevar/index.html')

def privacyPolicy(request):
    return render(request, 'reevar/privacy-policy.html')

def help(request):
    return render(request, 'reevar/help.html')