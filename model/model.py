
import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.DiGraph()
        self._idMapA = {}
    def getAllGeneri(self):
        return DAO.getAllGeneri()

    def creaGrafo(self):
        self._grafo.clear()
        self._idMapA.clear()