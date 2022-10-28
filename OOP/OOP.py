class Car():
    def __init__(self):
        self.__carlength = 200
        self.__carweigth = 1500
        self.__wheels = 4
        self.__rolling = False

    def start_car(self, starting):
        self.__rolling = starting
        if self.__rolling:
            checked = self.__internal_check()
        if(self.__rolling and checked):
            return "The car is rolling"
        elif(self.__rolling and checked == False):
            return "Something went wrong while checking the car"
        else:
            return "The car is not rolling"

    def state(self):
        print("The car has {0} wheels, its weight is {1} and its length is {2} "
            .format(self.__wheels,self.__carweigth, self.__carlength))

    def __internal_check(self):
        print("Performing internal checking")

        self.fuel = "OK"
        self.oil = "OK"
        self.doors = "closed"

        if(self.fuel == "OK" and self.oil == "OK" and self.doors == "closed"):
            return True
        else:
            return False



myCar = Car()

print(myCar.start_car(False))
myCar.state()

print("---------Now we create another instance---------")

myRenault = Car()

print(myRenault.start_car(True))
myRenault.state()

'''The initial values of the class variables are specified in a constructor
(constructor method)
its defined with 
def __init__(self):
in java for example the constructor has the same name of the class'''

'''To encapsulate a variable , so it is not accessible from outside the class
But it is still accessible from inside the class we use:
self.__wheels
inside the constructor 
'''

'''Encapsulate methods: ¿Utility?
Maybe to check the integrity of the car before start the engine
To encapsualte a method we can use the same way: __internal_check(self)
'''

