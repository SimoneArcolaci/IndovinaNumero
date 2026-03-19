from view import View
from model import Model
import flet as ft
class Controller(object): #E' il mediatore tra il modello e la view passa informazioni da una all'altro (aggiungendo inoltre alcune tipologie di controlli o operazioni più basilari rispetto a quelle svolte dal modello)
    def __init__(self, view: View): #Nel main quando creiamo l'oggetto di tipo controller gli passiamo la view (creata nella riga di comando prima)
        self._view = view
        self._model = Model() #Il model verrà chiamato solo dal controller, quindi lo generiamo direttamente in esso (sarebbe inutile generarlo nel main)
    def get_numeroMassimo(self):
        return self._model.Nmax
    def get_numeroTentativiMassimo(self):
        return self._model.Tmax
    def getTentativiRimanenti(self):
        return self._model.T
    #Le tre funzioni sopra servono per ottenere i valori delle variabili del modello (le quali vengono create quando viene inizializzato), stiamo di fatto chiamando le funzioni definite nella property
    def reset(self, e): #E' la funzione chiamata quando premo il bottone "Nuova Partita"
        self._model.reset() #Ri inizializzo le variabili ed estraggo un nuovo numero casuale dal modello
        self._view._txtTrimanenti.value = self._model.T #Reimposto il valore dei tentativi a 0
        self._view._txtInterattivo.value = "" #Svuoto il campo dove l'utente scrive
        self._view._lvOut.controls.clear() #Svuoto la tendina per i messaggi da quelli precedenti
        self._view._lvOut.controls.append(ft.Text("Indovina quale numero sto pensando.")) #Faccio comparire nella tendina il seguente messaggio (comparirà ogni volta che ri inizio il gioco)
        #Un append non accetta stringhe normali pertanto dobbiamo passargli un oggetto ft.Text("") con dentro la stringa che vogliamo visualizzzare
        self._view.update() #Carico la pagina
    def gioca(self, e): #E' la funzione chiamata quando premo il tasto "Gioca" (vale a dire quello col quale inserisco il valore nella casella di testo e lo passo al programma)
        tnt_str =self._view._txtInterattivo.value #E' la @property dell'oggetto TextField, vale a dire il contenuto scritto dall'utente
        try: #Inserisco un blocco Try, Except in quanto devo assicurarmi che il valore inserito sia quello corretto (un intero
            tnt = int(tnt_str)
        except ValueError:
            self._view._lvOut.controls.append(ft.Text("Devi inserire un numero intero", color = "red")) #Se il valore è sbagliato allora faccio comparire nella tendina il seguente messaggio
            self._view._lvOut.update() #E aggiorno
            return
        res = self._model.play(tnt) #Chiamo la funzione play del modello, la quale controllerà che il valore inserito sia corretto, maggiore o minore e restituirà un numero a seconda della casistica
        self._view._txtTrimanenti.value = str(self._model.T) #Aggiorno il valore della variabile dei tentativi in memoria
        if res == 0:
            self._view._lvOut.controls.append(ft.Text("Hai vinto", color="green"))
        if res == 2:
            self._view._lvOut.controls.append(ft.Text(f"Hai perso scemo! Il valore corretto era: {self._model.segreto}" , color="red"))
        if res == 1:
            self._view._lvOut.controls.append(ft.Text(f"Il valore inserito è minore di quello segreto", color="blue"))
        if res == -1:
            self._view._lvOut.controls.append(ft.Text(f"Il valore inserito è maggiore di quello segreto", color="purple"))
        self._view.update()
