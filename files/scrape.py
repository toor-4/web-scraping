#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

'''
# Send an HTTP GET request to the URL
url = "https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168"
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # ---- Save the content to a file -----
    with open("weatherForecast.html", "wb") as f:
        f.write(response.content)
    print("Page content saved to 'page_content.html'")
else:
    print("Failed to retrieve page content.")
'''
with open('weatherForecast.html','r', encoding='utf8') as f:
    file = f.read()
    soup = BeautifulSoup(file, 'lxml')
    
seven_days = soup.find_all('li', class_ = 'forecast-tombstone')
def weather_forecast():
    d, e, f, g = [],[],[],[]
    for seven_day in seven_days:
        # print(seven_day)
        period = seven_day.find('p', class_="period-name").text
        desc = seven_day.find('p', class_="short-desc").text
        temp  = seven_day.find('p', class_= "temp").text
        img = seven_day.find('img')['alt']
        d.append(period)
        e.append(desc)
        f.append(temp)
        g.append(img)
    return d, e, f, g

period,desc,temp,img = weather_forecast()

weather = pd.DataFrame({'Periods': period, 
        'Desc': desc,
        'Temp': temp,
        'Sum': img
        })
weather.to_csv('sevendaysFORECAST.csv',index=None)
print(weather)
print()
temperature = weather['Temp'].str.extract("(\d{2})", expand=False)
temperature = temperature.astype('int')
print(f'The Average Daily Temperature : int({temperature.values.mean()}) degrees')
print()

if __name__ == "__main__":
    weather_forecast()
