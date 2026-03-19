import flet as ft
from controller import Controller
from view import View
#Qui abbiamo il main che importa la view (il programma preposto alla realizzazione dell'interfaccia grafica)
#Il controller, il quale è il tramite tra il modello e la view (il modello elabora i dati, la view li mostra
#e questo viene mediato dal controller)
def main(page: ft.Page):
    v = View(page) #Creo la view e le passo il riferimento alla pagina fissa (page, la quale ora è come un foglio bianco)
    c = Controller(v) #Creo un oggetto della classe controller e gli passo la variabile della pagina, così che possa leggere quanto scritto dall'utente
    v.setController(c) #Così che, quando schiaccio un tasto della view, essa sappia quale funzione chiamare
    v.caricaInterfaccia()

ft.app(target=main)