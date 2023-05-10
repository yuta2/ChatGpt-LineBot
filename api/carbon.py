import os
import googlemaps
from datetime import datetime

# Google Maps API 金鑰
gmaps = googlemaps.Client(key = os.getenv("GMAPS_API_KEY"))

class Carbon:
    # def __init__(self):

    def calc_distance(self):
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

        print(f"距離：{distance} 公尺")
        print(f"時間：{duration} 秒")
