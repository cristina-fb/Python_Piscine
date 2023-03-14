import time

def ft_progress(lst):
    eta = 0
    i = 0
    max_space = 20
    length = len(lst)
    init_time = time.time()
    dig = len(str(length))
    for x in lst:
        i += 1
        percent = (i/length) * 100
        equals = int((percent * max_space) / 100) - 1
        arrow = (equals * '=') + '>' + (max_space - equals) * ' '
        et = time.time() - init_time
        print("ETA: "+ '{:.2f}'.format(eta) + "s [ " + '{:3d}'.format(percent) + " %][" + arrow + "] " + str(i) + "/" + str(length) + " | elapsed time " + '{:.2f}'.format(et) + "s")
        yield

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    #ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)