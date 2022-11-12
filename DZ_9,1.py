class Car():
    def __init__(self, car_brand, car_color, car_engine):
        self.car_brand=car_brand
        self.car_color=car_color
        self.car_engine=car_engine
    def drive_forward(self):
        print(self.car_brand+' drive_forward')
    def ride_back(self):
        print(self.car_brand+' ride_back')

class Car2(Car):
    def __init__(self):
        Car.__init__(self)
    def turn_left(self):
        print(self.car_brand+' turn_left')
    def turn_right(self):
        print(self.car_brand+' turn_right')

auto=Car('BMW','black','2.5')
auto.drive_forward()
auto.ride_back()
Car2.turn_right(auto)
Car2.turn_left(auto)
