

def final_price(price : float, discount : float):
    return price - price * discount / 100

def add_value(x : int, list_arg=[]):
    list_arg += [x]
    return list_arg

def add_value1(x : int, list_arg=None):
    if list_arg is None:
        list_arg = []
    list_arg += [x]
    return list_arg

def final_price1(price : float, discount : float):
    return price - price * discount / 100

def final_price2(*prices : int, discount=1):
    return [price - price * discount / 100 for price in prices]

def final_price3(*prices, discount=1, **kwargs):
    low = kwargs.get("price_low", min(prices))
    high = kwargs.get("price_high", max(prices))
    return [price - price * discount / 100 for price in prices if low <= price <= high]

def only_positive(x : int):
    return 0 < x

# result = filter(only_positive, [-1, 5, 6, -10, 0])
# print(", ".join(str(x) for x in result))

# result = filter(str.isalpha, "123ABcd")
# print("".join(result))

def square(x):
    return x ** 2

# result = map(square, range(1, 6))
# print(", ".join(str(x) for x in result))

# result = map(str.lower, ["abCD", "EFGh", "IJkl"])
# print("\n".join(result))

result = list(map(int, input().split()))
print(result)