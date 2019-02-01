import requests
import time
import random
import datetime

url = "http://localhost:8080/conditions"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'cache-control': "no-cache",
    }
cookies = {'JSESSIONID': '14BE5A168E4186796FB45377732B8B84'}

while True:
    temp=str(random.randint(-40, 40))
    hum=str(random.randint(30, 70))
    co2=str(random.randint(550, 850))
    currentDate=datetime.datetime.now()
    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"timestamp\"\r\n\r\n" + currentDate.strftime("%Y-%m-%d %H:%M:%S") + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"location\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"temp\"\r\n\r\n"+temp+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"hum\"\r\n\r\n"+hum+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"co2\"\r\n\r\n"+co2+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"_csrf\"\r\n\r\n3012f74c-81df-42fe-90e8-e9d839c852fd\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    response = requests.request("POST", url, data=payload, headers=headers, cookies=cookies)
    print(response.text)
    time.sleep(5)
