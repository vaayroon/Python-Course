'''
Inheritance lesson 1
'''


class Vehicles():
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model
        self.rolling = False
        self.accelerate = False
        self.brake = False

    def start_car(self):
        self.rolling = True

    def acelerate_car(self):
        self.accelerate = True

    def brake_car(self):
        self.brake = True

    def state(self):
        print("Brand: {0}\nModel: {1}\nRolling?: {2}\nAccelerating?: {3}\nbraking?: {4}"
              .format(self.brand, self.model, self.rolling, self.accelerate, self.brake))


class Motorbikes(Vehicles):
    pass


my_bike = Motorbikes("Honda", "CBR")

my_bike.state()

'''In short, for one object to inherit from another
we only need to pass that class as a parameter
'''

'''
Inheritance lesson 2
On method writing
Simple and multiple inheritance
'''
