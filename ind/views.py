from django.shortcuts import render

# Create your views here.
def virat(request):
    data='VIRAT KOHLI'
    data1='India Select Semi-Final To finals & Virat Took 117Runs To Win The Match... '
    d={'name':data,'win':data1}
    return render(request,'virat.html',context=d)