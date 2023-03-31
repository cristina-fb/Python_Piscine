import math
from statistics import quantiles
class TinyStatistician():
    def mean(self, x):
        sum = 0
        l = len(x)
        if l == 0:
            return None
        for i in x:
            sum += i
        return sum / l

    def median(self, x):
        l = len(x)
        if l == 0:
            return None
        x.sort()
        if l % 2 == 0:
            lst = (x[l//2 - 1], x[l//2])
            return self.mean(lst)
        return(x[l//2])

    def quartiles(self, x):
        l = len(x)
        if l == 0:
            return None
        x.sort()
        # if l % 2 == 0:
        # return [q1, q3]

    def var(self, x):
        l = len(x)
        if l == 0:
            return None
        m = self.mean(x)
        s = 0
        for i in x:
            s += (i - m)**2
        return s/l

    def std(self, x):
        l = len(x)
        if l == 0:
            return None
        return math.sqrt(self.var(x))

w = [23]
x = [1, 5, 2, 3]
y = [1, 42, 300, 10, 59]
z = []
tstat = TinyStatistician()
print("---- MEAN ----")
print(tstat.mean(w))
print(tstat.mean(x))
print(tstat.mean(y))
print(tstat.mean(z))
print("---- MEDIAN ----")
print(tstat.median(w))
print(tstat.median(x))
print(tstat.median(y))
print(tstat.median(z))
print("---- QUARTILES ----")
print(tstat.quartiles(w))
print(tstat.quartiles(x))
print(tstat.quartiles(y))
print(tstat.quartiles(z))
print("---- VAR ----")
print(tstat.var(w))
print(tstat.var(x))
print(tstat.var(y))
print(tstat.var(z))
print("---- STD ----")
print(tstat.std(w))
print(tstat.std(x))
print(tstat.std(y))
print(tstat.std(z))
