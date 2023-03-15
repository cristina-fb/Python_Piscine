import time, sys

def ft_progress(lst):
    eta = 0
    i=0
    max_space = 19
    length = len(lst)
    init_time = time.time()
    dig = len(str(length))
    for x in lst:
        i += 1
        percent = int((i/length) * 100)
        equals = int((percent * max_space) / 100)
        arrow = ((equals) * '=') + '>' + (max_space - equals) * ' '
        et = time.time() - init_time
        eta = (et * length) / i
        print("ETA: "+ '{:.2f}'.format(eta) + "s [ " + '{:3d}'.format(percent) + " %][" + arrow + "] " + "{:{}}".format(str(i), dig) + "/" + str(length) + " | elapsed time " + '{:.2f}'.format(et) + "s", end = '\r')
        yield i

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.005)
print()
print(ret)