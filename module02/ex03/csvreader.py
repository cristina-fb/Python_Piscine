import sys

class CsvReader:
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self):
        try:
            self.file = open(self.filename, 'r')
        except:
            self.__exit__("aaa", "aaaa", "aaaa")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        i = 0
        self.data = []
        for line in self.file:
            self.data.append(line.split(self.sep))
            if i == 0:
                self.n_data = len(self.data)
                i = 1
            else:
                if len(self.data[i]) != self.n_data:
                    print("A")
        return self.data[self.skip_top:len(self.data) - self.skip_bottom]

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        if self.header == True:
            return self.data[0]
        return None

with CsvReader('gooda.csv') as file:
    data = file.getdata()
    header = file.getheader()
    print(header)

# with CsvReader('bad.csv') as file:
#     if file == None:
#         print("File is corrupted")