from flask import Flask, request

import Moduuu

app = Flask(__name__)





@app.route('/webhook', methods=['POST'])

def webhook():

    print(type(request))

    req = request.get_json()    # 轉換成 dict 格式

    print(req)

    reText = req['queryResult']['fulfillmentText']   # 取得回覆文字

    intent = req['queryResult']['intent']['displayName']

    subadmin_area = req['queryResult']['parameters']['location'][0]

    print(subadmin_area['admin-area'])

    city_detector = Moduuu.city_detector(subadmin_area['admin-area'])

    weather_message = Moduuu.weather(city_detector)



    return {

          "fulfillmentText": f'{weather_message}',

          "source": "webhookdata"

      }



app.run(debug=True,port=5000)
