from django.shortcuts import render

def home(request):
    return render(request, "index.html")
def Andijon(request):
    return render(request, "Andijon.html")
def Fargona(request):
    return render(request, "fargona.html")
