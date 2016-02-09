from django.shortcuts import render
from graphos.sources.simple import  SimpleDataSource
from graphos.renderers import base, flot
import numpy as np
from .banditplay import FindCorr

# Create your views here.
def indexPage(request):
    if request.method == "POST":
         keywords = request.POST.get('keywords')
         keywords = keywords.split(',')
         try:
            x,y,bestarm = FindCorr(keywords)
         except:
            x = np.random.random_sample(5)
            y = np.random.random_sample(5)
            bestarm = 'tweet was not recieved so no'
         data = np.vstack([x,y]).T
         data = data.tolist()
         data.append(['X','Y'])
         data.reverse()
         dataSource = SimpleDataSource(data=data)
         rplot = flot.PointChart(dataSource)

         return render(request, 'explore/index.html', { 'rplot': rplot, 'bestarm': bestarm })# Create your views here.
    else:
         return render(request, 'explore/index.html')# Create your views here.

