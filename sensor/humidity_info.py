from house_info import HouseInfo
from datetime import date


class HumidityData(HouseInfo):
    def _convert_data(self, data):
        recs = []
