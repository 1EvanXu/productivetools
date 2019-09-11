
import csv


class DeviceInfo:

    def __init__(self, device: str, model: str, time_to_market: str, price: str):
        self.model = model  # 设备名称
        self.device = device  # 设备代号
        self._time_to_market = time_to_market  # 上市时间
        self._price = price  # 参考价格

    @property
    def price(self):
        return int(self._price)

    def __eq__(self, other):
        return self.device == other.device


class DevicesInfoLoader:

    price_lt_1000 = dict()
    price_btw_1000_and_2000 = dict()
    price_btw_2000_and_3000 = dict()
    price_mt_3000 = dict()

    @classmethod
    def load(cls, devices_info_file):

        with open(devices_info_file) as dif:
            read_result = csv.DictReader(dif)
            for row in read_result:
                d = row['device']
                m = row['model']
                t = row['time_to_market']
                p = row['price']
                device_info = DeviceInfo(d, m, t, p)
                if p < 1000:
                    cls.price_lt_1000[d] = device_info
                elif p < 2000:
                    cls.price_btw_1000_and_2000[d] = device_info
                elif p < 3000:
                    cls.price_btw_2000_and_3000[d] = device_info
                else:
                    cls.price_mt_3000[d] = device_info



