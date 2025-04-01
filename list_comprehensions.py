def list_comprehensions(): 
    numbers = [int(input()) for i in range(5)] # списочное выражение
    avg = sum(numbers) // len(numbers)
    numbers = [element for element in numbers if element > avg]
    print(numbers)

def maxtrix():
    matrix = [[int(x) for x in input().split()] for i in range(2)]
    print(matrix)

def list_comprehensions_into_dict():
    countries = {country: capital for country, capital in
             [("Россия", "Москва"),
              ("Беларусь", "Минск"),
              ("Сербия", "Белград")]}
    print(countries)