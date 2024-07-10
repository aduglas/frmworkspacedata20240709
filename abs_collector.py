from data import Data

class AbsCollector:



    def collect(self):
        None




class CsvCollector(AbsCollector):

    def collect(self):
        print("Collect d'un csv")


class CurlCollector(AbsCollector):

    def collect(self):
        print("Collect api")


class DataBaseCollector(AbsCollector):
    
    def collect(self):
        print("collect database")
