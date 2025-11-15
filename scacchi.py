caselle = [
    'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
    'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
    'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
    'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',
    'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
    'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
    'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'
]

posizioni_pezzi=[ #commenti == posizioni iniziali dei pezzi sulla scacchiera
#    pezzo , colonna (0-7), riga (0-7)   
    ['ra', 0, 0],  # Torre a8
    ['nb', 1, 0],  # Cavallo b8
    ['bc', 2, 0],  # Alfiere c8
    ['q', 3, 0],   # Regina d8
    ['k', 4, 0],   # Re e8
    ['bf', 5, 0],  # Alfiere f8
    ['ng', 6, 0],  # Cavallo g8
    ['rh', 7, 0],  # Torre h8
    ['pa', 0, 1],  # Pedone a7
    ['pb', 1, 1],  # Pedone b7
    ['pc', 2, 1],  # Pedone c7
    ['pd', 3, 1],  # Pedone d7
    ['pe', 4, 1],  # Pedone e7
    ['pf', 5, 1],  # Pedone f7
    ['pg', 6, 1],  # Pedone g7
    ['ph', 7, 1],  # Pedone h7
    
    ['Pa', 0, 6],  # Pedone a2
    ['Pb', 1, 6],  # Pedone b2
    ['Pc', 2, 6],  # Pedone c2
    ['Pd', 3, 6],  # Pedone d2
    ['Pe', 4, 6],  # Pedone e2
    ['Pf', 5, 6],  # Pedone f2
    ['Pg', 6, 6],  # Pedone g2
    ['Ph', 7, 6],  # Pedone h2
    ['Ra', 0, 7],  # Torre a1
    ['Nb', 1, 7],  # Cavallo b1
    ['Bc', 2, 7],  # Alfiere c1
    ['Q', 3, 7],   # Regina d1
    ['K', 4, 7],   # Re e1
    ['Bf', 5, 7],  # Alfiere f1
    ['Ng', 6, 7],  # Cavallo g1
    ['Rh', 7, 7]   # Torre h1
]

pezzi_bianchi = [
    'k',   # Re bianco
    'q',   # Regina bianco
    'ra', 'rh',  # Torri bianco
    'bc', 'bf',  # Alfieri bianco
    'nb', 'ng',  # Cavalli bianco
    'pa', 'pb', 'pc', 'pd', 'pe', 'pf', 'pg', 'ph'  # Pedoni bianco (colonne a-h)
]

pezzi_neri = [
    'k',   # Re nero
    'q',   # Regina nera
    'ra', 'rh',  # Torri nere
    'bc', 'bf',  # Alfieri neri
    'nb', 'ng',  # Cavalli neri
    'pa', 'pb', 'pc', 'pd', 'pe', 'pf', 'pg', 'ph'  # Pedoni neri (colonne a-h)
]

scacchiera = [
    ['r1', 'n1', 'b1', 'q', 'k', 'b2', 'n2', 'r2'],  # Riga 8 - Pezzi neri
    ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8'],  # Riga 7 - Pedoni neri
    ['·', '·', '·', '·', '·', '·', '·', '·'],  # Riga 6 - Vuota
    ['·', '·', '·', '·', '·', '·', '·', '·'],  # Riga 5 - Vuota
    ['·', '·', '·', '·', '·', '·', '·', '·'],  # Riga 4 - Vuota
    ['·', '·', '·', '·', '·', '·', '·', '·'],  # Riga 3 - Vuota
    ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'],  # Riga 2 - Pedoni bianchi
    ['R1', 'N1', 'B1', 'Q', 'K', 'B2', 'N2', 'R2']   # Riga 1 - Pezzi bianchi
]

pezzi_emojy = [
    ['♜', 'r'],
    ['♞', 'n'],
    ['♝', 'b'],
    ['♛', 'q'],
    ['♚', 'k'],
    ['♟', 'p'],
    ['♖', 'r'],
    ['♘', 'n'],
    ['♗', 'b'],
    ['♕', 'q'],
    ['♔', 'k'],
    ['♙', 'p'],
]

def mossa_valida(mossa):
    pass
    return True 

def leggi_mossa_bianco():
    print("\nTurno del bianco\n")
    pezzo=""
    mossa=""
    vincitore=""
    patta_proposta_bianco=0
    pezzo_emojy="none"
    
    while True:
        pezzo=input("Che pezzo vuoi muovere (inserisci solo l'iniziale) \n"
                    "Se vuoi proporre la patta scrivi patta\n" 
                    "Se vuoi arrenderti scrivi arresa\n")
        if pezzo == "patta": 
            patta_proposta_bianco=1
            break
        elif pezzo == "arresa":
            vincitore="nero"
            break
        elif pezzo in pezzi_bianchi:
            break
        print("Input non valido \n")

    if vincitore!="nero" and patta_proposta_bianco != 1:
        for i in range(len(pezzi_emojy)):   #trova l'emojy del pezzo scelto
            if pezzi_emojy[i][1] == pezzo[0]: #non guarda il colore
                pezzo_emojy = i
                break
        
        while True:
            mossa=input(f"Che mossa vuoi fare con il {pezzo} (es d5)")
            if mossa in caselle and mossa_valida(mossa)==True:
                break
            print("Input non valido ")
        for i in range (64):
            riga=i//8
            colonna=i%8
            if scacchiera[riga][colonna]==pezzo:
                scacchiera[riga][colonna]='·'                 #manca gestione cattura pezzi
                break
        
        # Converti la mossa in coordinate
        colonna_arrivo = ord(mossa[0]) - ord('a') # posizione arrivo
        riga_arrivo = 8 - int(mossa[1])
        
        for i in range(len(posizioni_pezzi)):  # trova la posizione di partenza del pezzo
            if posizioni_pezzi[i][0] == pezzo:
                riga_partenza = posizioni_pezzi[i][2]
                colonna_partenza = posizioni_pezzi[i][1]
 
        scacchiera[riga_partenza][colonna_partenza] = '·'
        scacchiera[riga_arrivo][colonna_arrivo] = pezzo_emojy

        posizioni_pezzi.remove([pezzo, colonna_partenza, riga_partenza])  # rimuovi la vecchia posizione del pezzo
        posizioni_pezzi.append([pezzo, colonna_arrivo, riga_arrivo])  # aggiorna la posizione del pezzo

    return vincitore, patta_proposta_bianco

def leggi_mossa_nero():
    print("\nTurno del nero\n")
    pezzo=""
    mossa=""
    vincitore=""
    patta_proposta_nero=0
    pezzo_emojy="none"
    
    while True:
        pezzo=input("Che pezzo vuoi muovere (inserisci solo l'iniziale) \n"
                    "Se vuoi proporre la patta scrivi patta\n" 
                    "Se vuoi arrenderti scrivi arresa\n")
        if pezzo == "patta": 
            patta_proposta_nero=1
            break
        elif pezzo == "arresa":
            vincitore="bianco"
            break
        elif pezzo in pezzi_bianchi:
            break
        print("Input non valido \n")

        if vincitore!="nero" and patta_proposta_nero != 1:
            for i in range(len(pezzi_emojy)):   #trova l'emojy del pezzo scelto
                if pezzi_emojy[i][1] == pezzo[0]: #non guarda il colore
                    pezzo_emojy = i
                    break
            
            while True:
                mossa=input(f"Che mossa vuoi fare con il {pezzo} (es d5)")
                if mossa in caselle:
                    break
                print("Input non valido ")

            for i in range (64):
                riga=i//8
                colonna=i%8
                if scacchiera[riga][colonna]==pezzo:
                    scacchiera[riga][colonna]='·'                 #manca gestione cattura pezzi
                    break
            
            # convert move like 'd5' to board indices (column a-h -> 0-7, row 8->0)
            col = ord(mossa[0]) - ord('a')
            row = 8 - int(mossa[1])
            scacchiera[row][col] = pezzi_emojy[pezzo_emojy][0]

    return vincitore, patta_proposta_nero

def stampa_scacchiera():
    print("\n    a   b   c   d   e   f   g   h\n")    # intestazione colonne
    for i in range(8):
        print(8 - i, "  ", end="")    # intestazione righe
        for j in range(8):
            for k in range(len(pezzi_emojy)):            # prova a trovare una corrispondenza basata sulla prima lettera (case-insensitive)
                emojy_corrispondente = '·'  # default se non trova corrispondenza
                if len(str(scacchiera[i][j])) > 0 and str(scacchiera[i][j])[0].lower() == pezzi_emojy[k][1]:
                    emojy_corrispondente = pezzi_emojy[k][0]
                    break
            print(emojy_corrispondente, "  ", end="")
        print("\n")
    print("\n")

def main():
    print("\nQuesto programma simula una partita di scacchi, un paio di cose prima di incominciare:\n-i nomi dei pezzi sono quelli in inglese quindi r per la torre, b per l'alfiere, n per il cavallo, p per il pedone, q per la regina e infine k per il re\n-se esistono piu di due pezzi uguali essi vengono chiamati con un numero come da esempio r2 --> la torre che all inizio della partita è nella casella A8\n-per i pezzi e per le caselle utilizza le lettere minuscole")
    vincitore=""
    patta_proposta_bianco=0
    patta_proposta_nero=0

    while True:
        stampa_scacchiera()
        vincitore,patta_proposta_bianco=leggi_mossa_bianco()
        if vincitore=="bianco" or vincitore=="nero":
            break
        if patta_proposta_bianco==1 and patta_proposta_nero==1:
            vincitore="patta"
            break
        stampa_scacchiera()
        vincitore,patta_proposta_nero=leggi_mossa_nero()
        if vincitore=="bianco" or vincitore=="nero":
            break
        if patta_proposta_bianco==1 and patta_proposta_nero==1:
            vincitore="patta"
            break

    print(f"\n!!!   Ha vinto il {vincitore}   !!!")

main()

# to do:

#bug da risolvere:
#- quando muovo un pezzo un altro sparisce o non succede nulla --> problema nella gestione della scacchiera
#-implementare locazione in tempo reale dei pezzi sulla scacchiera --> per sapere quale muovere --> camviare immissione pezzi utente --> gestita male tra lettere e numeri

#problemi da risolvere:

#-rifare array scacchiere con nome pezzi e poi quando stampi traduci in emojy
#-pedoni non per numero ma per colonna
#-commentare codice 

#funziopnalità mancanti:

#-gestione cattura pezzi
#-controllo mosse valide per ogni pezzo
#-gestione scacco e scacco matto
#-promozione pedone
#-arrocco
#-patta per richiesta di patta da entrambi i giocatori
#-altre patte (stallo, ripetizione mosse, 50 mosse senza cattura o movimento pedone)
#-en-passant
#-interfaccia grafica (coordinate caselle)
