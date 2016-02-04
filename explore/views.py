from django.shortcuts import render
from graphos.sources.simple import  SimpleDataSource
from graphos.renderers import base, flot
import numpy as np

# Create your views here.
def indexPage(request):
    if request.method == "POST":
         rval = float(request.POST.get('numvalue'))
         x = np.random.random_sample(5)
         y = x*rval
         data = np.vstack([x,y]).T
         data = data.tolist()
         data.append(['X','Y'])
         data.reverse()
         dataSource = SimpleDataSource(data=data)
         rval = flot.PointChart(dataSource)
         return render(request, 'explore/index.html', {'rval': rval})# Create your views here.
    else:
         return render(request, 'explore/index.html')# Create your views here.

