from django.shortcuts import render

# Create your views here.
def ODS(request):

    return render(request, 'ODS/ODS.html')