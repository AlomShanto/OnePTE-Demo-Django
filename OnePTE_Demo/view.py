from django.shortcuts import render


def start(request):
    return render(request, 'starting.html')

def home(request):
    return render(request, 'C:\\Users\suhayel\Desktop\OnePTE Demo\OnePTE_Demo\\templates\home.html')
