"""IF sentence, DEF methodo, and INPUT function"""
user_age = int(input("Please enter your age: "))
print("User age is", user_age)

"""Repasar ELSE ELIF"""

"""En python no existe switch?
    Concatenacion de operadores de comparacion
    operadores logicos and y or
    y el operador in"""

"""Como se evalua un flujo: if 0<x<100
    Primero evalua  0<x y si es falso pasa al siguiente comando, si es verdad evalua x<100
    Es decir lee de izquierda a derecha"""

salario = int(input("Enter your salary: "))
print("Your salary is: " + str(salario))
print("Your salary is: " + str(salario))

"""IN"""

asignatura = input("Enter a choice: ")
"We can use the method asignatura.lower(), to change the var into lowercase"
if asignatura in ("Electronica", "Robotica", "Automatizacion", "Control de Vehiculos"):
    print("La asignatura elegida es: " + asignatura)
else:
    print("La asignatura escogida no se corresponde con este plan")