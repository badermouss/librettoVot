import operator
from dataclasses import dataclass, field
from database.voti_dao import VotiDao

@dataclass(order=True)
# Order lo metto se voglio che vengano definiti i metodi __lt__, __gt__, ...
# Per default, i metodi di confronto vanno per ordine di definizione di attributi;
# In questo caso, di default ordina innanzitutto per esame.
class Voto:
    esame: str
    cfu: int
    punteggio: int
    lode: bool
    data: str = field(compare=False)

    def str_punteggio(self):
        """
        Costruisce la stringa che rappresenta in forma leggibile il punteggio tenendo conto della possibilità di lode:
        :return: 30 e lode oppure il punteggio sotto forma estetica
        """
        if self.punteggio == 30 and self.lode:
            return "30 e lode"
        else:
            return f"{self.punteggio}"

    def copy(self):
        """
        Costruisce la copia di un oggetto Voto
        :return: oggetto Voto
        """
        return Voto(self.esame, self.cfu, self.punteggio, self.lode, self.data)

    def __str__(self):
        return f"{self.esame} ({self.cfu} CFU): voto {self.punteggio} in {self.data}"


class Libretto:
    def __init__(self):
        self._voti = []
        self._voti_dao = VotiDao()

    def append(self, voto):
        if not self.hasConflitto(voto):
            self._voti.append(voto)
        else:
            return

    def media(self):
        if len(self._voti) == 0:
            raise ValueError("Elenco voti vuoti")
        punteggi = [v.punteggio for v in self._voti]  # creo una lista fatta di punteggi
        return sum(punteggi) / len(punteggi)

    def __str__(self):
        return f"Numero voti: {len(self._voti)}"

    def findByPunteggio(self, punteggio, lode):
        """
        Seleziona i soli esami che hanno un punteggio definito
        :param punteggio: punteggio dell'esame
        :param lode: boolean
        :return: lista di oggetti di tipo voto
        """
        corsi = []
        for v in self._voti:
            if v.punteggio == punteggio and v.lode == lode:
                corsi.append(v)
        return corsi

    def findByCorso(self, esame):
        for v in self._voti:
            if v.esame == esame:
                return v

    def hasVoto(self, voto):
        """
        Esiste già un esame con lo stesso nome e lo stesso punteggio
        :param voto: oggetto voto
        :return: True se esiste
        """
        for v in self._voti:
            if v.esame == voto.esame and v.punteggio == voto.punteggio and v.lode == voto.lode:
                return True
        return False

    def hasConflitto(self, voto):
        for v in self._voti:
            if v.esame == voto.esame and not (v.punteggio == voto.punteggio and v.lode == voto.lode):
                return True
        return False

    def copy(self):
        nuovo = Libretto()
        for v in self._voti:
            nuovo._voti.append(v.copy())
        return nuovo

    def creaMiglioramento(self):
        """
        Crea una copia del libretto e migliora i voti in esso presenti
        :return: oggetto Libretto "migliorato"
        """
        nuovo = self.copy()

        """
        nuovo._voti[0] == self._voti[0]
        Due riferimenti diversi per lo stesso oggetto
        """
        for v in nuovo._voti:
            if 18 <= v.punteggio <= 23:
                v.punteggio += 1
            elif 24 <= v.punteggio <= 28:
                v.punteggio += 2
            elif v.punteggio == 29:
                v.punteggio = 30
        return nuovo

    def crea_ordinato_per_esame(self):
        nuovo = self.copy()
        nuovo.ordina_per_esame()
        return nuovo

    def ordina_per_esame(self):
        # ordina self._voti per esame
        self._voti.sort(key=lambda v: v.esame)
        # self._voti.sort(key=operator.attrgetter('voto'))

    def crea_ordinato_per_punteggio(self):
        nuovo = self.copy()
        nuovo.ordina_per_punteggio()
        return nuovo

    def ordina_per_punteggio(self):
        self._voti.sort(key=lambda v: (v.punteggio, v.lode), reverse=True)

    def stampa(self):
        print(f"Hai {len(self._voti)} voti")
        for v in self._voti:
            print(v.__str__())
        print(f"La media vale {self.media()}")

    def stampaGUI(self):
       outList = [f"Hai {len(self._voti)} voti"]
       for v in self._voti:
          outList.append(v)
          outList.append(f"La media vale {self.media():.2f}")
       voti = self._voti_dao.get_voti()
       return outList


    """
    Opzione 1: creo metodo stampa_per_nome e metodo stampa_per_punteggio, che semplicemente stampano
    e non modificano nulla
    
    Opzione 2: metodo crea_libretto_ordinato_per_nome e un metodo crea_libretto_ordinato_per_punteggio, che creano 
    delle copie separate, sulle quali potrò chiamare il metodo stampa
    
    Opzione 3: metodo ordina_per_nome che modifica il libretto originale e poi analogamente il metodo
    ordina_per_punteggio, poi userò metodo stampa
    + aggiungiamo gratis un metodo copy()
    
    Opzione 2bis: crea una copia shallow (che contiene i riferimenti all'oggetto e non oggetti copiati) del libretto
    
    La migliore è l'OPZIONE 3 
    """

    def cancella_inferiori(self, punteggio):
        """for v in self._voti:
            if v.punteggio < punteggio:
                self._voti.remove(v)"""

        # molto più veloce
        # mentre itero, non devo ASSOLUTAMENTE modificare la lista sulla quale sto iterando
        """for i in range(len(self._voti)):
            if self._voti[i].punteggio < punteggio:
                self._voti.pop(i)"""

        """for v in self._voti:
            if v.punteggio >= punteggio:
                voti_nuovi.append(v)"""
        voti_nuovi = [v for v in self._voti if v.punteggio >= punteggio]

        self._voti = voti_nuovi


# potrei scrivere del codice qua per testare
def _test_voto():
    print(__name__)


if __name__ == "__main__":
    _test_voto()
