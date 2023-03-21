import copy
class Vector:
    def __init__(self, values):
        self.values = values
        if len(values) == 1:
            self.shape = (1, len(values[0]))
        else:
            self.shape = (len(values), 1)
    
    def __str__(self):
        return(str(self.values))

    def __repr__(self):
        return(str(self.values))

    def __add__(self, n):
        aux = copy.deepcopy(self)
        if isinstance(n, int) or isinstance(n, float):
            if len(aux.values) == 1:
                for i in range(len(aux.values[0])):
                    aux.values[0][i] += n
            else:
                for i in aux.values:
                    i[0] += n
        elif isinstance(n, Vector) and self.shape == n.shape:
            if len(aux.values) == 1:
                for i in range(len(aux.values[0])):
                    aux.values[0][i] += n.values[0][i]
            else:
                for i, j in zip(aux.values, n.values):
                    i[0] += j[0]
        else:
            print("ERROR!")
            return None
        return aux

    def __sub__(self, n):
        aux = copy.deepcopy(self)
        if isinstance(n, int) or isinstance(n, float):
            if len(aux.values) == 1:
                for i in range(len(aux.values[0])):
                    aux.values[0][i] -= n
            else:
                for i in aux.values:
                    i[0] -= n
        elif isinstance(n, Vector) and self.shape == n.shape:
            if len(aux.values) == 1:
                for i in range(len(aux.values[0])):
                    aux.values[0][i] -= n.values[0][i]
            else:
                for i, j in zip(aux.values, n.values):
                    i[0] -= j[0]
        else:
            print("ERROR!")
            return None
        return aux

    def __mul__(self, n):
        aux = copy.deepcopy(self)
        if isinstance(n, int) or isinstance(n, float):
            if len(aux.values) == 1:
                for i in range(len(aux.values[0])):
                    aux.values[0][i] *= n
            else:
                for i in aux.values:
                    i[0] *= n
        else:
            print("ERROR!")
            return None
        return aux

    def __truediv__(self, n):
        aux = copy.deepcopy(self)
        if isinstance(n, int) or isinstance(n, float):
            if len(aux.values) == 1:
                for i in range(len(aux.values[0])):
                    try:
                        aux.values[0][i] /= n
                    except:
                        print("ERROR!")
                        return None
            else:
                for i in aux.values:
                    try:
                        i[0] /= n
                    except:
                        print("ERROR!")
                        return None
        else:
            print("ERROR!")
            return None
        return aux

    def T(self):
        if len(self.values) == 1:
            ret = []
            for i in self.values[0]:
                aux = []
                aux.append(i)
                ret.append(aux)
        else:
            ret = []
            aux = []
            for i in self.values:
                aux.append(i[0])
            ret.append(aux)
        return Vector(ret)
            
    def dot(self, a):
        if not isinstance(a, Vector):
            print("ERROR!")
            return None
        if self.shape != a.shape:
            print("ERROR!")
            return None
        dot = 0
        if (len(a.values) == 1):
            aux1 = self.T()
            aux2 = a.T()
        else:
            aux1 = self
            aux2 = a
        for i, j in zip(aux1.values, aux2.values):
            dot += i[0] * j[0]
        return(dot)
