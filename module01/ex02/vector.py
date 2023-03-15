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
        print(self)

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
            ret.append[aux]
        return ret
            
    def dot(self, a):
        if type(a) != Vector:
            print("ERROR!")
            return None
        if self.shape != a.shape:
            print("ERROR!")
            return None
        dot = 0
        for i, j in zip(self.values, a.values):
            dot += i[0] * j[0]
        return(dot)
