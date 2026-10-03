import flet as ft


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def fillDDGeneri(self):
        try:
            generi= self._model.getAllGeneri()
            for y in generi:
                self._view._ddGenre.options.append(ft.dropdown.Option(y))
                   # key=actor.id,
                  #  text=actor.name))
            self._view.update_page()

        except Exception as ex:
            self._view._txt_result.controls.append(
                ft.Text(f"Errore nel recupero dei generi: {ex}", color="red") )
            self._view.update_page()


    def handleCreaGrafo(self, e):
        genere = self._view._ddGenre.value

        if not genere:
            self._view.create_alert("Selezionare un genere prima di creare il grafo.", color="red")
            return

        try:
            self._model.creaGrafo(genere)
            n_nodes = self._model.get_num_nodes()
            n_edges = self._model.get_num_edges()

            # Stampa immediata numero di vertici e archi (Punto 1.c)
            self._view._txt_result.controls.append(
                ft.Text(f"Grafo creato con successo!\nNumero vertici: {n_nodes}\nNumero archi: {n_edges}", color="green"))

            # RIEMPIO IL DROPDOWN DEI FILM DEL GRAFO
            self.fillDDFilm()

        except Exception as ex:
            self._view._txt_result.controls.append(
                ft.Text(f"Errore durante la creazione del grafo: {ex}", color="red")
            )
            #return
        self._view.update_page()

    def handleStampaInfo(self, e):
        self._view._txt_result.controls.clear()

        numero, largest,film_max_out, max_out,  details = self._model.getConnessaInfo()
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Il grafo contiene {numero} componenti connesse\n", color="green"))
        self._view._txt_result.controls.append(ft.Text(f"Film con maggior numero archi uscenti: {film_max_out} (archi uscenti: {max_out})\n" , color="green"))
        self._view._txt_result.controls.append(ft.Text(f"La componente connessa maggiore ha dimensione in numero di film {len(largest)}\n"))

        for titolo, numero_attori in details:
            self._view._txt_result.controls.append(
                ft.Text(f"{titolo}: {numero_attori} attori"))
        self._view.update_page()

    def fillDDFilm(self):
        try:

            film= self._model.getFilmGrafo()
            for y in film:
                self._view._ddMovie.options.append(ft.dropdown.Option(y.title))
                   # key=actor.id,
                  #  text=actor.name))
            self._view.update_page()

        except Exception as ex:
            self._view._txt_result.controls.append(ft.Text(f"Errore nel recupero dei film: {ex}", color="red") )
            self._view.update_page()

    def handleTrovaSelezione(self, e):
        self._view._txt_result.controls.clear()
        k = self._view._txtInN.value
        # qui dovremmo fare i solti controlli sulla validità

        try:
            kInt = int(k)
        except Exception as ex:
            self._view._txt_result.controls.append(
                ft.Text(f"Errore ! devi inserire un intero per procedere: {ex}", color="red")
            )
            self._view.update_page()
            return
        if kInt <= 0:
            self._view.create_alert(
                "N deve essere un intero positivo.",  color="red"   )
            return

        # recupero l'attore selezionato dal Dropdown
        start_node = self._model._idMapF[self._view._ddMovie.value]

        if self._view._ddMovie.value is None:
            self._view.create_alert("Selezionare prima un FILM di partenza.", color="red")
            return

        listFilm, bestScore = self._model.getGruppoFilm(start_node, kInt)

        if listFilm is None:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text(
                f"Non ci sono abbastanza comoonenti connesse per trovare N film", color="red"))
            return
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(
            f" Di seguito il Gruppo di N film ADIACENTI, massimizzando il numero di film:", color="green"))
        for p in listFilm:
            self._view._txt_result.controls.append(ft.Text(p))
        self._view.update_page()


    