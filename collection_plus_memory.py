from sys import getsizeof
from timeit import timeit
from copy import deepcopy

### immutable type of data:
# int 
# float
# str
# tuple
# frozenset  
### mutable
# set
# list
# dict

def get_list():
    list = [1, 2, "3", 23.4] # mutable
    print(list)

def get_tuple():
    tuple = (1, 2, "3", 23.4) # aka immutable list
    print(tuple) 

def ordered_collections():
    text = "Привет, мир!"
    list_symbols = list(text) # [...]
    tuple_symbols = tuple(text) # (...)
    text_from_list = str(list_symbols) # [...]
    print(text)
    print(list_symbols)
    print(tuple_symbols)
    print(text_from_list)
    
def get_set():
    word = "collection"
    letters = set(word)
    print(letters)

def union_set():
    set1 = {1, 3, 5, 7}
    set2 = {2, 4, 6, 8}
    print(set1 | set2)
    print(set1.union(set2))

def intersection_set():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    print(set1 & set2)
    print(set1.intersection(set2))

def use_set():
    vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}
    letters = set("коллекция")
    print(", ".join(letters & vowels))

def get_dict():
    countries_and_capitals = {"Россия": "Москва",
                          "США": "Вашингтон",
                          "Франция": "Париж"}
    # print(countries_and_capitals["Франция"])
    # print(countries_and_capitals["Сербия"]) # KeyError
    return countries_and_capitals

def use_dict():
    for country in get_dict():
        print(f"У страны \"{country}\" столица - {get_dict()[country]}")

def get_size_of():
    number_iter = (i for i in range(10 ** 6))
    print(f"Итератор занимает {getsizeof(number_iter)} байт.")
    number_list = list(range(10 ** 6))
    print(f"Список занимает {getsizeof(number_list)} байт.")

def compare_join():
    print(round(timeit("s = '; '.join(str(x) for x in range(10 ** 7))", number=10), 3))
    print(round(timeit("s = '; '.join([str(x) for x in list(range(10 ** 7))])", number=10), 3))

def learn_memory():
    x = 5
    print(f"id(x = 10): {id(x)}")
    x = 10
    print(f"id(x = 15): {id(x)}")

def learn_memory1():
    x = 1
    print(f"id(x) = {id(x)}")
    y = 2
    print(f"id(y) = {id(y)}")
    print(f"x is y: {x is y}")
    y = x
    print(f"id(x) = {id(x)}")
    print(f"id(y) = {id(y)}")
    print(f"x is y: {x is y}")

def mutable_types_of_data():
    numbers = [112, 231 , 42]
    print(f"{numbers}, id = {id(numbers)}")
    numbers = numbers + [25] 
    # numbers += [24]
    # numbers.append(23)
    print(f"{numbers}, id = {id(numbers)}")

def learn_memory2():
    x = [1, 2, 3]
    y = x
    print(f"x is y: {x is y}")
    print(f"y is x: {y is x}")
    x[0] = 0
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"x is y: {x is y}")
    print(f"y is x: {y is x}")

def learn_memory3():
    numbers = [[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 1, 2, 3]]
    # numbers_copy = numbers[:]
    numbers_copy = numbers.copy()
    print(f"numbers is numbers_copy: {numbers is numbers_copy}")
    print(f"numbers_copy[i] is numbers[i]", [numbers_copy[i] is numbers[i] for i in range(len(numbers))])

def learn_memory4():
    numbers = [[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 1, 2, 3]]
    # numbers_copy = [item[:] for item in numbers]
    numbers_copy = deepcopy(numbers)
    print(f"numbers is numbers_copy: {numbers is numbers_copy}")
    print(f"numbers_copy[i] is numbers[i]", [numbers_copy[i] is numbers[i] for i in range(len(numbers))])