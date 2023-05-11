# CODE TO RETRIEVE DATA FROM THE WEATHER API AND STORE IT IN A CSV FILE
# FROM 2019/01/01 TO 2022/12/31

import requests
import time
import datetime as dt
import csv 

key = 'enJH8FUX2z5Ar7NSCJvYI8pAIuDW0XDV9nbSkEMj'

start_date = dt.date(2019, 1, 1)
end_date = dt.date(2022, 12, 31)

assert start_date < end_date, 'Start date must be before end date'

delta = dt.timedelta(days=1)

freq = 1/20

day = start_date

columns = ['timestamp', 'mm_precip', 'temperature']

with open('weather_data/weather.csv', mode = 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=columns)
    writer.writeheader()

    while day <= end_date:

        day_string = day.strftime('%Y/%m/%d')

        url = 'https://api.meteo.cat/xema/v1' + '/estacions/mesurades/X8/' + day_string 

        print(day_string)

        headers = {'Accept': 'application/json', 'X-API-KEY': key}

        data = requests.get(url, headers=headers).json()[0]

        # the codi variables, 35 and 32, correspond to precipitation and temperature respectively. The json file retrieved
        # contains information on many more variables, but we are only interested in these two.

        precipitation = [data['variables'][i]['lectures'] for i in range(len(data['variables'])) if data['variables'][i]['codi'] == 35][0]
        temperature = [data['variables'][i]['lectures'] for i in range(len(data['variables'])) if data['variables'][i]['codi'] == 32][0]

        date_variables = [{'timestamp':int(dt.datetime.strptime(d['data'], '%Y-%m-%dT%H:%MZ').timestamp()), 'mm_precip':d['valor']} for d in precipitation]

        for i in range(len(date_variables)):
            date_variables[i]['temperature'] = temperature[i]['valor']

        writer.writerows(date_variables)

        day += delta

        time.sleep(freq)
