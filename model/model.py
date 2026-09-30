
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

    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

    def get_num_nodes(self) -> int:
        return self._grafo.number_of_nodes()

    def get_num_edges(self) -> int:
        return self._grafo.number_of_edges()
