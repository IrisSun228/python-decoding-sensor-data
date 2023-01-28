from house_info import HouseInfo
from datetime import date


class HumidityData(HouseInfo):
    def _convert_data(self, data):
        recs = []

        for rec in data:
            # Convert string of integers into actual integers based 10
            recs.append(float(rec) * 100)

        return recs
