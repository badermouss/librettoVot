from UI.view import View
from modello.voto import Libretto
from modello.voto import Voto
import flet as ft


class Controller(object):
    def __init__(self, view: View, libretto: Libretto):
        self._view = view
        self._model = libretto
        self.startUpLibretto()

    def handleAdd(self, e):
        nomeEsame = self._view._txtIn.value
        if nomeEsame == "":
            self._view._lvOut.controls.append(ft.Text("Il campo nome non può esser vuoto", color="red"))
            self._view.update()
            return

        strCfu = self._view._txtCFU.value
        try:
            intCfu = int(strCfu)
        except ValueError:
            self._view._lvOut.controls.append(ft.Text("Il campo CFU deve essere un intero", color="red"))
            self._view.update()
            return

        punteggio = self._view._ddVoto.value

        if punteggio is None:
            self._view._lvOut.controls.append(ft.Text("Il campo punteggio va selezionato", color="red"))
            self._view.update()
            return

        if punteggio == "30L":
            punteggio = 30
            lode = True
        else:
            punteggio = int(punteggio)
            lode = False

        data = self._view._datePicker.value # data è un oggetto di tipo datetime
        if data is None:
            self._view._lvOut.controls.append(ft.Text("Seleziona una data", color="red"))
            self._view.update()
            return

        self._model.append(Voto(nomeEsame, intCfu, punteggio, lode,
                                f"{data.year}-{data.month}-{data.day}"))
        self._view._lvOut.controls.append(ft.Text("Voto correttamente aggiunto.", color="green"))
        self._view.update()






    def handlePrint(self, e):
        outList = self._model.stampaGUI()
        for element in outList:
            self._view._lvOut.controls.append(ft.Text(element))
        self._view.update()

    def startUpLibretto(self):
        self._model.append(Voto("Fisica I", 10, 25, False, "2022-06-25"))
        self._model.append(Voto("Analisi II", 10, 30, True, "2023-01-30"))
        self._model.append(Voto("Informatica", 8, 22, False, "2022-01-29"))
        self._model.append(Voto("Chimica", 8, 26, False, "2022-02-05"))
        self._model.append(Voto("Analisi I", 10, 28, False, "2022-01-25"))
