from django.shortcuts import render

# Create your views here.
def kane(request):
    data='KANE WILLIAMSON'
    data1='New Zealand Team Loose To Finals By Indian Team...'
    d={'name':data,'loose':data1}
    return render(request,'kane.html',context=d)