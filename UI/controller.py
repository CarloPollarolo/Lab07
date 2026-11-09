import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        biblioteche = self._model.get_biblioteche()
        if biblioteche:
            for b in biblioteche:
                self._view.dropdown_biblioteca.options.append(ft.dropdown.Option(b.nome))

        generi = self._model.get_generi()
        if generi:
            for g in generi:
                self._view.dropdown_genere.options.append(ft.dropdown.Option(g))

    # CALLBACKS DROPDOWN
    def cambia_biblioteca(self, e):  #attivata dopo aver selzionato nel dd
        biblio = self._view.dropdown_biblioteca.value

        if biblio != "Nessun filtro":
            self.biblioteca_selezionata = biblio
        else:
            self.biblioteca_selezionata = None

    def cambia_genere(self, e):  #attivata dopo aver selzionato nel dd
        gen = self._view.dropdown_genere.value

        if gen != "Nessun filtro":
            self.genere_selezionato = gen
        else:
            self.genere_selezionato = None

    # AZIONE: MOSTRA LIBRI
    def mostra_libri(self, e):
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)
        self._view.lista_libri.controls.clear()

        if libri is None:
            self._view.show_alert("Impossibile connettersi al database")

        elif len(libri) == 0:
            self._view.show_alert("Nessun libro trovato con i filtri selezionati")

        else:
            for libro in libri:
                self._view.lista_libri.controls.append(ft.Text(str(libro)))

        self._view.update()