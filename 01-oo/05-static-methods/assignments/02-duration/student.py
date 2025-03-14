
class Duration:

    def __init__(self,seconds):
        self.seconds = seconds

    @property
    def seconds(self):
        return self.__seconds
    
    @property 
    def minutes(self):
        return self.__seconds
    
    @property
    def hours(self):
        return self.seconds /3600
    
    @seconds.setter
    def seconds(self,amount):
        self.__seconds = amount
    

    @staticmethod
    def from_seconds(seconds):
        return Duration(seconds)
            
    @staticmethod
    def from_minutes(seconds):
        return Duration(seconds * 60)
    
    @staticmethod
    def from_hours(seconds):
        return Duration(seconds * 3600)

duration = Duration.from_hours(2)



print(duration.seconds)
print(duration.hours)

# print(duration = Duration.from_minutes(10))