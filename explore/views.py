from django.shortcuts import render

# Create your views here.
def indexPage(request):
    if request.method == "POST":
         rval = 'Sebbs chos hast'#float(request.POST.get('numvalue'))**2
    else:
         rval = 'Sebbs chos hast'
    return render(request, 'explore/index.html', {'rval': rval})# Create your views here.
