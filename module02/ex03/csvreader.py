class CsvReader:
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        if filename == None or isinstance(filename) != str:
            return
    def __enter__():

    def __exit__():
        
    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """