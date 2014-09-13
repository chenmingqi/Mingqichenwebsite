from django.shortcuts import render
from django.http import HttpResponse
#from reportlab.pdfgen import canvas

# Create your views here.
def homepage(request):
    '''
    show the homepage of mingqi's personal website.
    '''
    if request.method == "GET":
        return render(request,"index.html",{})
'''
def resume(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

    if request.method == "GET":
        return response
'''