def ft_reduce(function_to_apply, iterable):
    try:
        if len(iterable) == 1:
            return iterable[0]
        for i in range(1, len(iterable)):
            if  i == 1:
                res = function_to_apply(iterable[0], iterable[i])
            else:
                res = function_to_apply(res, iterable[i])
        return res
    except:
        print("ERROR!")
    return None


lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(ft_reduce(lambda u, v: u + v, lst))
nums = [1]
print(ft_reduce(lambda x, y: x + y, nums))
nums = [1, 2, 3, 4]
print(ft_reduce(lambda x, y: x + y, nums))
print(ft_reduce(lambda x, y: x + y, 33))
print(ft_reduce(lambda x: x + 3, nums))
print(ft_reduce("lambda x, y: x + y", nums))