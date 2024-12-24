import requests
from django.shortcuts import render
from datetime import datetime
import pytz

def index(request):
    weather_data = []
    error_message = None
    
    if request.method == "POST":
        city_name = request.POST.get('name')
        api_key = "0c42f7f6b53b244c78a418f4f181282a"  # استبدل بـ API Key الخاص بك
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            city = data["name"]
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            icon = data["weather"][0]["icon"]
            timezone = data["timezone"]
            dt_utc = datetime.utcfromtimestamp(data["dt"])  # UTC time

            # تحويل UTC إلى الوقت المحلي
            city_timezone = pytz.timezone(str(pytz.country_timezones(data["sys"]["country"])[0]))
            local_time = pytz.utc.localize(dt_utc).astimezone(city_timezone)

            weather_data.append({
                "city": city,
                "temperature": temperature,
                "description": description,
                "icon": icon,
                "local_time": local_time.strftime('%Y-%m-%d %H:%M:%S')
            })
        else:
            error_message = "لم يتم العثور على المدينة، يرجى المحاولة مرة أخرى"
    
    return render(request, 'index.html', {'weather_data': weather_data, 'error_message': error_message})