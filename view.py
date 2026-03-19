import flet as ft
from flet_core import TextField

#Questa classe ha il compito di di gestire direttamente l'interfaccia utente
class View(object):
    def __init__(self, page):
        self._page = page
        self._page.title = "TdP 2024 - Indovina il Numero"
        self._page.horizontal_alignment = 'CENTER'
        self._titolo = None
        self._controller = None

    def caricaInterfaccia(self): #Essa verrà chiamata all'avvio, caricando tutta l'interfaccia
        self._titolo = ft.Text("Indovina il numero",
                               color="blue", size=24) #Compare in alto a sinistra nella pagina ed è il titolo di essa
        self._txtNmax = ft.TextField(label="Numero max",value=self._controller.get_numeroMassimo(), disabled=True) #TextField da il riquadro caratterestico con il contorno all'oggetto della pagina, inoltre in esso si potrebbe scrivere ma disabled = True lo rende un oggetto statico
        self._txtTmax = ft.TextField(label="Tentativi Max", value=self._controller.get_numeroTentativiMassimo(), disabled= True) #I valori per questi pulsanti vengono indicati dal controller il quale li prende controllando nel modello
        self._txtTrimanenti = ft.TextField(label="Numero tentativi rimanenti", value=self._controller.getTentativiRimanenti(), disabled=True)
        self._txtInterattivo = ft.TextField(label="Valore") #Questo non ha disabled, pertanto all'interno ci possiamo scrivere, nel programma è dove andremo ad inserire il valore che proviamo ad indovinare
        self._btnReset = ft.ElevatedButton(text="Nuova Partita", on_click=self._controller.reset) #Creo un bottone su cui posso cliccare (esso chiama una funzione definita nel controller per riavviare la partita in questo caso)
        self._btnGioca = ft.ElevatedButton(text="Gioca", on_click=self._controller.gioca)
        self._lvOut = ft.ListView(expand = True) #Crea una tendina per messaggi non contornata e non interagibile, è dove compariranno i nostri messaggi nell'interfaccia (ad esempio "Hai vinto", "Numnero troppo basso" ecc...)
        self._lvOut.controls.append(ft.Text("Indovina quale numero sto pensando."))#Faccio comparire il messaggio (dal momento che altrimenti quando apro il programma dovrei premere nuova partita prima di vederlo
        self._row1 = ft.Row(controls=[self._txtNmax, self._btnReset]) #Creo le righe della flet (se non specificato hanno una grandezza pre impostata) e dico quali elementi (TextField, Buttons ecc...) mettere nella riga
        self._row2 = ft.Row(controls=[self._txtTrimanenti, self._txtTmax])
        self._row3 = ft.Row(controls=[self._txtInterattivo, self._btnGioca])
        self._page.add(self._row1, self._row2, self._row3, self._lvOut) #Una volta definiti le righe le vado infine ad agggiungere alla pagina (che in principio era un foglio bianco), questa informazione è salvata nella memoria ma non viene visualizzata fino al comando update

        


        self._page.update() #Carica gli aggiornamenti della pagina

    def setController(self,controller): #Passo alla view il controller (dal momento che esso gli deve passare ad esempio i campi dei TextField) così sà quale programma chiamare
        self._controller = controller #Passo alla view

    def update(self):
        self._page.update() #Sarà utile al controller quando aggiorna la pagina a caricare i vari aggiornamenti rendendoli visualizzabili