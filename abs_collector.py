from data import Data
import pandas as pd

class AbsCollector:

    instanceData:Data = None

    def collect(self):
        None




class CsvCollector(AbsCollector):

    nomFichier:str = ""

    def __init__(self, filePath):
        self.nomFichier = filePath

    def collect(self):
        print("Collect d'un csv")
        self.instanceData = Data()
        self.instanceData.instanceDataFrame = pd.read_csv(self.nomFichier)

class CurlCollector(AbsCollector):

    def collect(self):
        print("Collect api")


class DataBaseCollector(AbsCollector):
    
    def collect(self):
        print("collect database")
