from django.shortcuts import render

# Create your views here.
def indexPage(request):
    if request.method == "POST":
         rval = float(request.POST.get('numvalue'))**2
    else:
         rval = ''
    return render(request, 'toyApp/index.html', {'rval': rval})# Create your views here.
