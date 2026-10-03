
import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._grafo = nx.DiGraph()
        self._idMapF = {}

    def getAllGeneri(self):
        return DAO.getAllGeneri()

    def creaGrafo(self, genere):
        self._grafo.clear()
        self._idMapF.clear()

        movie = DAO.getAllNodes(genere)
        for a in movie:
            self._idMapF[a.id] = a
            self._grafo.add_node(a)
            # aggiungo i nodi
        print("2 - Nodi aggiunti")
       # self._grafo.add_nodes_from(movie)

        cast = DAO.getCastFilm(genere)
        print("3 - Cast caricato:", len(cast))

        for row in cast:
            film = self._idMapF[row[0]]
            film.attori.append((row[1]))
        print("4 - Attori aggiunti ai film")

            # SE NON AVESSI USATO LE TUPLE, MA SOLO ROW NEL DAO
        # actor = self._idMapA[row["name_id"]] #recupero dall'idMap
        # actor.movies.append(
        #   (row["title"], row["year"], row["avg_rating"]))

        for i in  range(len(movie)): #NON POSSO ACCEDERE DIRETTAMENTE, perchè movie è una lista!
            f1 = movie[i]
            for j in range(i + 1,len(movie )):
                f2 = movie[j]

                # Condividono almeno un attore nel cast
                if  set(f1.attori) & set(f2.attori):
                    y1 = f1.year
                    y2 = f2.year

                    # Se anno uguale oppure almeno uno non specificato (None) -> 2 archi
                    if y1 is None or y2 is None or y1 == y2:
                        self._grafo.add_edge(f1, f2)
                        self._grafo.add_edge(f2, f1)
                    elif y1 < y2:
                        self._grafo.add_edge(f1, f2)
                    else:
                        self._grafo.add_edge(f2, f1)
        print("5 - Archi creati:", self._grafo.number_of_edges())


    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

    def get_num_nodes(self) -> int:
        return self._grafo.number_of_nodes()

    def get_num_edges(self) -> int:
        return self._grafo.number_of_edges()

    def getConnessaInfo(self):
        #lo trasformo in non orientato pk richiesto di ignorare
        grafo_non_orientato = self._grafo.to_undirected()
        components = list(nx.connected_components(grafo_non_orientato))
        #components = list(nx.connected_components(self._grafo))  # TROVO LE COMP CONNESSE e ci faccio una lista
        largest = max(components, key=len)  # trova la + grande

        # b. Film con maggior numero di archi uscenti
        film_max_out = max(self._grafo.nodes,  key=lambda n: self._grafo.out_degree(n) )
        #relativo numero archi usenti
        max_out = self._grafo.out_degree(film_max_out)


        #ORDINO PER  NUMERO ATTORI!!
        ordered_nodes = sorted(largest, key=lambda n: len(n.attori), reverse=True) #ordine decrescente
        details = [(n,  len(n.attori)) for n in ordered_nodes]

        return len(components), largest,film_max_out, max_out, details

