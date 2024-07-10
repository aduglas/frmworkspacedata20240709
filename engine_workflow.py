from abs_collector import *


def run():
    instanceCollector: AbsCollector = None
    # mise en place du collector
    # instanceCollector = CsvCollector() 
    instanceCollector = CurlCollector() 

    # todo mise en place des autres éléments du workflow

    # appel collect de la donné
    instanceCollector.collect()

