import os
import googlemaps
from datetime import datetime
import json

# Google Maps API 金鑰
gmaps = googlemaps.Client(key = os.getenv("GMAPS_API_KEY"))

class Carbon:
    @classmethod
    def __init__(self):
        pass

    def calc_distance():
        # 輸入起點和終點的地址或座標
        origin = '彰化市彰水路186號'
        destination = '基隆內港'

        # 設置查詢參數，例如交通方式、出發時間等等
        mode = 'driving'  # 可選值：'driving'、'walking'、'bicycling'、'transit'
        departure_time = datetime.now()

        # 呼叫 Google Maps API 並取得路徑距離
        directions_result = gmaps.directions(origin,
                                             destination,
                                             mode=mode,
                                             departure_time=departure_time)

        distance = directions_result[0]['legs'][0]['distance']['value']
        duration = directions_result[0]['legs'][0]['duration']['value']

        data = {
            'distance': distance,
            'duration': duration,
            'status': 'OK'
        }
        return json.dumps(data)

