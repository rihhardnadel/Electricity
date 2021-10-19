import requests
import json
from datetime import datetime, timedelta

from requests.api import get

def get_data():
    today = datetime.now() - timedelta(hours=3)
    tomorrow = today + timedelta(days=1)
    actual_tomorrow = tomorrow.replace(hour=0)

    start = f'{today.strftime("%Y")}-{today.strftime("%m")}-{today.strftime("%d")} {today.strftime("%H")}:{today.strftime("%M")}'
    end = f'{tomorrow.strftime("%Y")}-{tomorrow.strftime("%m")}-{tomorrow.strftime("%d")} {tomorrow.strftime("%H")}:{today.strftime("%M")}'

    URL = f"https://dashboard.elering.ee/api/nps/price?start={start}&end={end}"

    response = requests.get(URL)

    data = json.loads(response.content.decode())["data"]["ee"]
    return data




def format_data(data):
    new_data = []

    for datapoint in data:
        actual_hour = datetime.utcfromtimestamp(datapoint["timestamp"]) + timedelta(hours=2)
        dic = {"timestamp" : actual_hour.strftime("%H:%M"), "price" : datapoint["price"]}
        new_data.append(dic)

    print(new_data)
    return new_data

if __name__ == "__main__":
    data = get_data()
    new_data = format_data(data)