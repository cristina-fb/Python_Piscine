import copy

def ft_map(function_to_apply, iterable):
    cpy = copy.deepcopy(iterable)
    try:
        for i in range(0, len(cpy)):
            cpy[i] = function_to_apply(cpy[i])
    except:
        print("ERROR!")
        return None
    return cpy

x = [1, 2, 3, 4, 5]
print(ft_map(lambda dum: dum + 1, x))
print(x)
print(ft_map(lambda dum: dum + 1, 33))
print(ft_map("lambda dum: dum", x))
print(ft_map(lambda: 1, x))