from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import BankDetails


# Create your views here.
@csrf_exempt 
def index(req):
    data = json.loads(req.body)
    print(data)
    response = {}
    if 'name' in data.keys() and 'city' in data.keys():
        response = BankDetails.objects.filter(bank_name=data['name'],bank_city=data['city']).values()
    elif 'isfc' in data.keys():
        response = BankDetails.objects.filter(bank_ifsc=data['isfc']).values()
    return HttpResponse(response)