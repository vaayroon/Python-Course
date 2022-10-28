from xml.etree.ElementTree import SubElement


def even_function_generator(limit):
    """Function that generates numbers until a limit

    Args:
        limit (integer): The limit number

    Returns:
        list: List with the generated numbers
    """
    i = 1
    mylist = []
    while i < limit:
        mylist.append(i * 2)
        i += 1
    return mylist


def even_generator(limit):
    """Generator function that generates numbers until a limit
    Yield builds an iterable object

    Args:
        limit (integer): The limit number

    Yields:
        generator: Generator with the generated numbers
    """
    i = 1
    while i < limit:
        yield i * 2
        i += 1


print(even_function_generator(8))
returned_even = even_generator(9)
#print(returned_even)  # It just prints the value as "<generator object even_generator at 0x000001CDCD152F20>"
'''for i in returned_even:
    print(i)'''
#Insted of printing all the varibles with the next() function where are saying that we only want 
#the first value and so on
#between calls, the generator stay in stand by so you resources
#With the list all the values are generated
#with the generator does not generate all values and does not reserve memory space
print(next(returned_even))
print("Here it can be more code")
print(next(returned_even))
print("Here it can be more code")

'''
    Generator II: instruction YIELD FROM
'''

def return_cities(*cities):
    """Generator function that

    Args:
        cities (tuple): Not determinated(*) number of elements

    Yields:
        _type_: _description_
    """
    for element in cities:
        #for subelement in element:
            #yield subelement
            yield from element


# for subelement in element:
# instead using another for loop to obtain the letters of the element
# we can use 'yield from'
# With YIELD it return all the elemnts
# with YIELD FROM it returns the letter of a element(subelement)

returned_cities = return_cities("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(returned_cities))
print("Here it can be more code")
print(next(returned_cities))
