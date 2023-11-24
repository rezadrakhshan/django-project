from django.shortcuts import render
from league.models import Table
# Create your views here.


def home(request):
    table = Table.objects.all()
    context = {'table':table}
    return render(request,"index.html",context)