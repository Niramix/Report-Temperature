
#Install Library for time
#pip install schedule

#Import library and create fuction
import schedule
from datetime import datetime
import time
import requests

#apikey = '58e256a70c60f35e4dfe03f3b27c94cd'

#city = ("Chiang Mai")

#url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}'

#data = requests.get(url).json()

#temp = data['main']['temp'] - 273.15 #Change temp to degree C

#print(f"{temp:.2f}")


def job():
    
    apikey = '58e256a70c60f35e4dfe03f3b27c94cd'

    city = ("Chiang Mai")

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}'

    data = requests.get(url).json()

    temp = data['main']['temp'] - 273.15 #Change temp to degree C
    
    print('Time : ',datetime.now(),"Chiang Mai Temperature :",f"{temp:.2f}") 

#Create command every 5 min and while loop
job()
schedule.every(5).minutes.do(job)

while True:
    
    schedule.run_pending()
    time.sleep(1)
    

