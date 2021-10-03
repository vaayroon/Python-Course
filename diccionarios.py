"""Se hace una asociacion CLAVE : VALOR
    La clave es unica. Dentro de esta se puede almacenar Tuplas, Listas e incluso diccionarios"""

mydict = {"Alemania": "Berlin", "Francia": "Paris","UK": "Londres","España": "Madrid"}
print(mydict)

"Agregar elementos a un diccionario ya creado"
mydict["Italia"]="Lisboa"
print(mydict)

"Modificar el valor de una clave / simplemente se sobreescribe. Nunca va a haber dos calves con el mismo nombre"
mydict["Italia"]="Roma"
print(mydict)

"Eliminar un elemento / Se usa el metodo DEL"
del mydict["UK"]
print(mydict)

"--------------------"

mydict2 = {"Alemania": "Berlin", 23: "Jordan", "Mosqueteros": 3}
print(mydict2)

"Añadir una tupla a un diccionario"
mitupla=["España", "Francia", "UK", "Alemania"]
mydict3 = {mitupla[0]: "Madrid", mitupla[1]: "Paris", mitupla[2]: "Londres", mitupla[3]: "Berlin"}
print(mydict3)

"Para acceder a elementos en concreto"
print(mydict3["España"])

"Asignar una tupla a un valor"
mydict4 = {23: "Jordan", "Nombre": "Michael", "Equipo": "Chicago", "anillos": [1991, 1992, 1993, 1996, 1997, 1998]}
print(mydict4)
"Acceder a los valores del valor tupla"
print(mydict4["anillos"])

"Diccionario dentro de un diccionario"
mydict4 = {23: "Jordan", "Nombre": "Michael", "Equipo": "Chicago", "anillos": {"temporadas": [1991, 1992, 1993, 1996, 1997, 1998]}}
print(mydict4["anillos"])
print("")
print(mydict4.keys())
print(mydict4.values())
print(len(mydict4))
print(mydict4["anillos"].keys())
print(mydict4["anillos"].values())
print(len(mydict4["anillos"]))
