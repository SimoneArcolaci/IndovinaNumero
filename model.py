import random

class Model(object):
    def __init__(self):
        self._Nmax = 100
        self._Tmax = 6
        self._segreto = None
        self._T = self._Tmax
        self.reset()
#Definiamo una classe modello (essa è il cuore operativo del programma, dove si devono svolgere
#le funzioni necessarie al funzionamento)

    def reset(self, e=None):
        self._segreto = random.randint(0,self._Nmax)
        self._T = self._Tmax
#Ogni volta che resettiamo il programma deve estrarre un numero casuale e riportare il numero dei tentativi
#_T al numero massimo impostato _Tmax
    def play(self, tentativo):
        """
        tentativo == segreto return 0
        tentativo < segreto return 1
        tantetivo > segreto return -1
        tentativo è oltre Tmax allora return 2
        """
        self._T -= 1
        if tentativo == self._segreto:
            return 0
        if self._T == 0:
            return 2
        elif tentativo < self._segreto:
            return 1
        elif tentativo > self._segreto:
            return -1
        else:
            return 2
#E' la funzione preposta al controllo del parametro inserito dall'utente, il quale verrà confrontato con il valore
#estratto a caso e sulla base di esso ritornerà dei valori che verranno poi interpretato dal controller (il tramite)
    @property
    def Nmax(self):
        return self._Nmax
    @property
    def Tmax(self):
        return self._Tmax
    @property
    def segreto(self):
        return self._segreto
    @property
    def T(self):
        return self._T
#Varie funzioni per il recupero delle variabili (le quali avendo _ davanti sarebbero nascoste all'esterno

if __name__ == "__main__":
    m = Model()
    m.reset()
