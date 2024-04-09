from voto import Libretto, Voto

lib = Libretto()
v1 = Voto("Analisi I", 10, 28, False, "2022-01-25")
lib.append(v1)

lib.append(Voto("Fisica I", 10, 25, False, "2022-06-25"))
lib.append(Voto("Analisi II", 10, 30, True, "2023-01-30"))
lib.append(Voto("Informatica", 8, 22, False, "2022-01-29"))
lib.append(Voto("Chimica", 8, 26, False, "2022-02-05"))

voti25 = lib.findByPunteggio(25, False)
for v in voti25:
    print(v.esame)

voto_esame = lib.findByCorso("Analisi II")
print(f"Voto esame di {voto_esame.esame}: {voto_esame.str_punteggio()}")

v2 = Voto("Fisica I", 10, 28, False, "2022-06-25")
lib.append(v2)
print(lib.hasVoto(v2))

migliorato = lib.creaMiglioramento()
lib.append(Voto("Tesi", 3, 0, False, "2024-06-29"))

lib.stampa()
print()
migliorato.stampa()

ordinato = lib.crea_ordinato_per_esame()
ordinato.stampa()

ordinato_punteggio = lib.crea_ordinato_per_punteggio()
ordinato_punteggio.stampa()

print("Dopo che ho cancellato:")
lib.cancella_inferiori(27)
lib.stampa()
