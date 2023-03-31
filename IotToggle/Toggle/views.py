from django.shortcuts import render
from django.http import JsonResponse
import requests
from boltiot import Bolt
# Create your views here.

def index(request):
    return render(request,'index.html')

def toggle_led(request):
    api_key = "92159781-c86c-491b-b169-4c62c1411c70"
    device_id = "BOLT13624928"
    mybolt = Bolt(api_key, device_id)
    if request.method == 'GET' and 'toggle' in request.GET:
        led_on = request.GET['toggle'] == 'on'
        if led_on:
            response = requests.get('https://cloud.boltiot.com/remote/ed248704-57fb-48fd-8dd5-f3f745cfacee/digitalWrite?deviceName=BOLT13624928&pin=0&state=HIGH')
            message = 'LED turned on!'
            print(response)
            print(message)
        else:
            response = requests.get('https://cloud.boltiot.com/remote/ed248704-57fb-48fd-8dd5-f3f745cfacee/digitalWrite?deviceName=BOLT13624928&pin=0&state=LOW')
            message = 'LED turned off!'
            print(response)
            print(message)
        return JsonResponse({'message': message})
    return JsonResponse({})
