import flet as ft

from UI.view import View
from UI.controller import Controller
from modello.voto import Libretto


def main(page: ft.Page):
    v = View(page)  # è l'unico che conosce la pagina
    lb = Libretto()
    c = Controller(v, lb)  # è l'unico che può parlare sia con il View che con il modello (Voto)
    v.setController(c)
    v.caricaInterfaccia()


ft.app(target=main)
