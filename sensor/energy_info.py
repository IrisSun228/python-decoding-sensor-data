from house_info import HouseInfo
from datetime import date


class EnergyData(HouseInfo):
    ENERGY_PER_BULB = 0.2
    ENERGY_BITS = 0x0F0

    def _get_energy(self, rec):
        energy = int(rec, base=16)
        energy = energy & self.ENERGY_BITS
        energy = energy >> 4
        return energy
