import copy

def ft_filter(function_to_apply, iterable):
    cpy = copy.deepcopy(iterable)
    try:
        for i in cpy:
            if not function_to_apply(i):
                cpy.remove(i)
    except:
        print("ERROR!")
        return None
    return cpy

x = [1, 2, 3, 4, 5]
print(ft_filter(lambda dum: not (dum % 2), x))
print(x)
print(ft_filter(lambda dum: not (dum % 2), 333))
print(ft_filter("lambda dum: not (dum % 2)", x))
print(ft_filter(lambda: dum + 1, x))