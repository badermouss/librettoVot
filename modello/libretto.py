from dataclasses import dataclass

"""
class Voto:
    def __init__(self, esame, cfu, punteggio, lode, data):
        self.esame = esame
        self.cfu = cfu
        self.punteggio = punteggio
        self.lode = lode
        self.data = data

        if self.lode and self.punteggio != 30:
            raise ValueError("Lode non applicabile")

    def __str__(self):  # DUNDER
        return f"Esame {self.esame} superato con {self.punteggio}"

    def __repr__(self):
        return f"Voto({self.esame}, {self.punteggio}, {self.cfu}, {self.lode}, {self.data})"
"""


# si può usare dataclass per creare una classe "boilerplate", cioè più completa dove i metodi principali sono già
# definiti di default
@dataclass
class Voto:
    esame: str
    cfu: int
    punteggio: int
    lode: bool
    data: str


class Libretto:
    def __init__(self):
        self._voti = []

    def append(self, voto):
        self._voti.append(voto)

    def media(self):
        if len(self._voti) == 0:
            raise ValueError("Elenco voti vuoti")
        punteggi = [v.punteggio for v in self._voti]  # creo una lista fatta di punteggi
        return sum(punteggi) / len(punteggi)

    def __str__(self):
        return (f"Numero v"
                f"oti: {len(self._voti)}")


voto_1 = Voto("Analisi Matematica I", 10, 28, False, "2022-01-25")
voto_2 = Voto("Basi di Dati", 8, 30, True, "2023-01-26")

print(voto_1)  # avendo usato __str__ funziona anche così
print(voto_1.__str__())

print(voto_1, voto_2)
miei_voti = [voto_1, voto_2]
print(miei_voti)

mio_libretto = Libretto()
mio_libretto.append(voto_1)
mio_libretto.append(voto_2)

print(mio_libretto)
print(f"Media: {mio_libretto.media()}")
