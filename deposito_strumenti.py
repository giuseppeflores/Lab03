import csv
from operator import attrgetter
from strumenti_e_prestiti import Strumento
from strumenti_e_prestiti import Prestito

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO

        self.__nome = nome
        self.__responsabile = responsabile
        self.strumenti = []
        self.prestiti = []

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO

        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for riga in reader:
                if riga:
                    s = Strumento(riga[0].strip(), riga[1].strip(), riga[2].strip(), int(riga[3].strip()),
                                  float(riga[4].strip()))
                    self.strumenti.append(s)

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO

        num = len(self.strumenti) + 1
        id_strumento = f"S{num}"
        s = Strumento(id_strumento, tipo, marca, anno_acquisto, valore)
        self.strumenti.append(s)
        return s

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO

        return sorted(self.strumenti, key=attrgetter('marca'))

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO

        strumento_trovato = None
        for s in self.strumenti:
            if s.id_strumento == id_strumento:
                strumento_trovato = s
                break

        if not strumento_trovato:
            raise Exception("Errore: Strumento non trovato nel sistema.")

        for p in self.prestiti:
            if p.id_strumento == id_strumento:
                raise Exception("Errore: Lo strumento è già in prestito.")

        num = len(self.prestiti) + 1
        id_prestito = f"P{num}"
        p = Prestito(id_prestito, data, id_strumento, cognome_allievo)
        self.prestiti.append(p)
        return p

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO

        for p in self.prestiti:
            if p.id_prestito == id_prestito:
                self.prestiti.remove(p)
                return
        raise Exception("Errore: ID prestito non valido.")
