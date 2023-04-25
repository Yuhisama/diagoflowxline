import requests

import json

def city_detector(city_input):

    json_api = {"宜蘭縣":"宜蘭縣","桃園市":"桃園市","新竹縣":"新竹縣","苗栗縣":"苗栗縣",

            "彰化縣":"彰化縣","南投縣":"南投縣","雲林縣":"雲林縣","嘉義縣":"嘉義縣",

            "屏東縣":"屏東縣","臺東縣":"臺東縣","花蓮縣":"花蓮縣","澎湖縣":"澎湖縣",

            "基隆市":"基隆市","新竹市":"新竹市","嘉義市":"嘉義市","臺北市":"臺北市",

            "高雄市":"高雄市","新北市":"新北市","臺中市":"臺中市","臺南市":"臺南市",

            "連江縣":"連江縣","金門縣":"金門縣"}

    city = city_input

    location_name = city

    if location_name in json_api.keys():

        location_code = json_api[location_name]

        return location_code

    else:

        candidates = [name for name in json_api.keys() if name.startswith(location_name)]

        if len(candidates) > 0:

            location_code = json_api[candidates[0]]

            return location_code

        else:

            print("error")

            

def weather(city):

    url = "" #change your url



    response = requests.get(url)

    data = json.loads(response.text)



    locations = data["cwbopendata"]["dataset"]["location"]



    city_name = city



    cityname = [city for city in locations if city['locationName'] == city_name][0]



    city = cityname['locationName']    # 縣市名稱

    wx8 = cityname['weatherElement'][0]['time'][0]['parameter']['parameterName']    # 天氣現象

    maxt8 = cityname['weatherElement'][1]['time'][0]['parameter']['parameterName']  # 最高溫

    mint8 = cityname['weatherElement'][2]['time'][0]['parameter']['parameterName']  # 最低溫

    ci8 = cityname['weatherElement'][3]['time'][0]['parameter']['parameterName']    # 舒適度

    pop8 = cityname['weatherElement'][4]['time'][0]['parameter']['parameterName']   # 降雨機率

    return (f'{city}未來 8 小時{wx8}，最高溫 {maxt8} 度，最低溫 {mint8} 度，降雨機率 {pop8} %')