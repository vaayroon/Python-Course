------------------------------PARADIGM---------------------------------------------

--POP vs OOP--

---¿Object? --> car

    *Has attributes: Colour, weight, height, large
    *Has a behavior: start, brake, turn, speed up

--Advantages

    *Modular
    *Reusable, inheritance
    *The program does not break if something goes wrong
    *Encapsulation

--Vocabulary

    *Class --> Chassis of Car
    *Instance --> Object belonging to a class
    *Modularization
     |-->  *Encapsulation --> All classes are connected to work, but probably 1 class has no idea what is inside another
                              and cannot be accessible from outside
        You can create access methods to connect classes, so that they work together

--Example:

    *accessing object properties:
        mycar.color="red";
        mycar.weight=1500;
    *accessing object behaviour
        mycar.start();
        mycar.brake();
        mycar.accelerate();