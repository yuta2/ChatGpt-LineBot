import os
import googlemaps
from datetime import datetime
import json
import math

# Google Maps API 金鑰
gmaps_keys = os.getenv("GMAPS_API_KEY")
gmaps = googlemaps.Client(key = gmaps_keys)

class Carbon:
    # @classmethod
    # def __init__(self):
    #     pass

    # 透過google maps獲取距離
    def calc_distance(origin, destination):
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
            'from': origin,
            'to': destination,
            'distance': distance,
            'distance_unit': 'km',
            'duration': duration,
            'duration_unit': 'second',
            'status': 'OK'
        }
        return json.dumps(data) / 1000  # km

    #
    # def get_geocode_location(address):
    #     """使用Google Maps API獲取地址的經緯度"""
    #
    #     # Google Maps API的URL
    #     url = 'https://maps.googleapis.com/maps/api/geocode/json'
    #
    #     # 構建參數字典
    #     params = {
    #         'address': address,
    #         'key': gmaps_keys
    #     }
    #
    #     # 發送GET請求
    #     response = requests.get(url, params=params)
    #
    #     # 解析JSON數據
    #     json_data = response.json()
    #
    #     # 檢查請求是否成功
    #     if json_data['status'] == 'OK':
    #         # 獲取經度和緯度
    #         lat = json_data['results'][0]['geometry']['location']['lat']
    #         lng = json_data['results'][0]['geometry']['location']['lng']
    #         return (lat, lng)
    #     else:
    #         return None
    #
    #
    # def distance_on_unit_sphere(lat1, long1, lat2, long2):
    #     """計算兩個地址之間的大圓航線距離"""
    #
    #     # 將經度和緯度轉換為弧度
    #     degrees_to_radians = math.pi / 180.0
    #
    #     # 將緯度和經度換算成弧度
    #     phi1 = (90.0 - lat1) * degrees_to_radians
    #     phi2 = (90.0 - lat2) * degrees_to_radians
    #     theta1 = long1 * degrees_to_radians
    #     theta2 = long2 * degrees_to_radians
    #
    #     # 計算cos和sin值
    #     cos = (math.sin(phi1) * math.sin(phi2) * math.cos(theta1 - theta2) +
    #            math.cos(phi1) * math.cos(phi2))
    #
    #     # 計算兩點間的距離
    #     arc = math.acos(cos)
    #
    #     # 在地球半徑上縮放弧長，得到距離
    #     return arc * 6371  #
    #
    # def km_to_mi(km):
    #     return km / 1.609344
    #
    # def km_to_nm(km):
    #     return km / 1.852
    #
    # def distance_to_carbon_emissions(distance_km, transportation):
    #     if transportation == 'airplane':
    #         return distance_km * 0.285  # 歐盟環境署（EEA）的估算
    #     elif transportation == 'ship':
    #         return distance_km * 0.040  # 國際海事組織（IMO）的估算
    #     # 定義各種車輛的碳排放係數（kg CO2 / km）
    #     elif transportation == 'car':
    #         return distance_km * 0.170  # 小型汽車
    #     elif transportation == 'suv':
    #         return distance_km * 0.250  # 運動型多功能車(休旅車)
    #     elif transportation == 'bus':
    #         return distance_km * 0.089  # 巴士
    #     elif transportation == 'minivan':
    #         return distance_km * 0.181  # 小型商用車
    #     elif transportation == 'delivery':
    #         return distance_km * 0.200  # 貨車
    #     elif transportation == 'truck':
    #         return distance_km * 0.005  # 卡車
