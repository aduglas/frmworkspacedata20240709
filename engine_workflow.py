from abs_collector import *
from data import Data

def run():
    instanceCollector: AbsCollector = None
    # mise en place du collector
    instanceCollector = CsvCollector("./lesdonnees/data.csv") 
    # instanceCollector = CurlCollector() 

    # todo mise en place des autres éléments du workflow

    # appel collect de la donné
    instanceCollector.collect()
    # recuperation de Data
    innerData:Data = instanceCollector.instanceData

