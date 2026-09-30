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
        genre = self._view._ddGenre.value

        if not genre:
            self._view.create_alert("Selezionare un genere prima di creare il grafo.")
            return

        

    def handleStampaInfo(self, e):
        pass

    def handleTrovaSelezione(self, e):
        pass

    