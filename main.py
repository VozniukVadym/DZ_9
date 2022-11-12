class Car():
    def __init__(self, car_brand, car_color, car_engine):
        self.car_brand=car_brand
        self.car_color=car_color
        self.car_engine=car_engine
    def drive_forward(self):
        print('drive_forward')
    def ride_back(self):
        print('ride_back')
audi=Car('audi','a6','2.5')
audi.drive_forward()
audi.ride_back()
