import os
import googlemaps
from datetime import datetime
import json
import math

# Google Maps API 金鑰
gmaps = googlemaps.Client(key = os.getenv("GMAPS_API_KEY"))

class Carbon:
    # @classmethod
    # def __init__(self):
    #     pass

    # 透過google maps獲取距離
    def calc_distance(origin_text, destination_text, mode_text):
        # 輸入起點和終點的地址或座標
        origin = origin_text
        destination = destination_text
        # mode = 'driving'  # 可選值：'driving'、'walking'、'bicycling'、'transit'
        mode = mode_text if mode_textmode_text else "driving"
        # 設置查詢參數，例如交通方式、出發時間等等
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
            'distance_unit': 'meter',
            'duration': duration,
            'duration_unit': 'second',
            'status': 'OK'
        }
        return json.dumps(data)

    def distance_on_unit_sphere(lat1, long1, lat2, long2):

        # 將經度和緯度轉換為弧度
        degrees_to_radians = math.pi / 180.0

        # 將緯度和經度換算成弧度
        phi1 = (90.0 - lat1) * degrees_to_radians
        phi2 = (90.0 - lat2) * degrees_to_radians

        theta1 = long1 * degrees_to_radians
        theta2 = long2 * degrees_to_radians

        # 計算cos和sin值
        cos = (math.sin(phi1) * math.sin(phi2) * math.cos(theta1 - theta2) +
               math.cos(phi1) * math.cos(phi2))

        # 計算兩點間的距離
        arc = math.acos(cos)

        # 在地球半徑上縮放弧長，得到距離
        return arc * 6371