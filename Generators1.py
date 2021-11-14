def even_function_generator(limit):
    i = 1
    mylist = []
    while i < limit:
        mylist.append(i * 2)
        i += 1
    return mylist


def even_generator(limit):
    i = 1
    while i < limit:
        yield i * 2
        i += 1


print(even_function_generator(8))
returned_even = even_generator(9)
print(returned_even)  # It just prints the value as "<generator object even_generator at 0x000001CDCD152F20>"
'''for i in returned_even:
    print(i)'''

print(next(returned_even))
print("Here it can be more code")
print(next(returned_even))
print("Here it can be more code")


def return_cities(*cities):
    for element in cities:
        yield from element


# for subelement in element:
# instead using another for loop to obtain the letters of the element
# we can user 'yield from'


returned_cities = return_cities("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(returned_cities))

print(next(returned_cities))
