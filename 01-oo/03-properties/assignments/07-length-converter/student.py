

class LengthConverter():

    def __init__(self):
        self.__distance_in_meter = 0

    @property
    def meter(self):
        return self.__distance_in_meter
    
    @meter.setter
    def meter(self, value):
        self.__distance_in_meter = value
        

    @property
    def feet(self):
        return self.__distance_in_meter * 3.28
    
    @feet.setter
    def feet(self, value):
        self.__distance_in_meter = value * 0.3048
        

    @property
    def inch(self):
        return self.__distance_in_meter/0.0254
    
    @inch.setter
    def inch(self, value):
        self.__distance_in_meter = value * 0.0254

# converter = LengthConverter()

# converter.meter = 100

# print(converter.meter)