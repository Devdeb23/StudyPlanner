import sqlite3

# FUNZIONE: AGGIUNGI ESAME
def aggiungi_esame(): # Crea la funzione per aggiungere in modo corretto l'esame
    print("\n--- Aggiungi un nuovo esame ---") # Stampa l'intestazione della sezione

    # Chiediamo all'utente di inserire i dati dell'esame
    # Input accoglie la variabile  inserita dall'utente e la tiene da parte
    nome = input("nome dell'esame: ") # Salva la variabile nome

    data = input("Data dell'esame (yyyy-mm-dd)") # Salva la variabile data

    cfu = int(input("QUanti CFU vale l'esame? ")) # Salva la variabile cfu come intero
        # int() converte la stringa digitata dall'utente in un numero intero per poterla calcolare
    paragrafi_totali = int(input("Quanti paragrafi totali ha il materiale da studiare? ")) # Salva la variabile paragrafi_totali come intero

    # Connessione al database
    conn = sqlite3.connect('study_planner.db') # Mi collego al database esistente
    cursore = conn.cursor() # Creo un cursore per eseguire i comandi SQL 
    # Il cursore è un oggetto che permette di interagire con il database

    # Eseguo il comando SQL per inserire i dati nella tabella esami
    # Userò i punti di domanda (?) come segnaposto per i valori da inserire per evitare SQL injection
    # SQL injection è una tecnica usata dagli hacker per manipolare i database attraverso input malevoli

    cursore.execute('''
                    INSERT INTO esami (nome, data_scadenza, cfu, paragrafi_totali)
                    VALUES (?, ?, ?, ?)
                    ''', (nome, data, cfu, paragrafi_totali)) # Passo i valori da inserire come una tupla 
    
    conn.commit() # Salvo le modifiche nel database
    conn.close() # Chiudo la connessione al database
    print(f"Ottimo! Hai aggiunto l'esame di '{nome}' al tuo piano di studio con successo.") # Messaggio di conferma all'utente

#FUNZIONE: VISUAZZA TUITI GLI ESAMI
def visualizza_esami(): # Crea la funzione per visualizzare gli esami
    print("\n-- Lista Esami --") # Stampa l'intestazione della sezione
    conn = sqlite3.connect('study_planner.db') # Mi collego al databse dove si trovano gli esami
    cursore = conn.cursor() # Creo un cursore per eseguire i comandi SQL

    cursore.execute('SELECT * FROM esami') # Eseguo la selezione di tutti gli esami dalla tabella esami
    esami = cursore.fetchall() # Recupero tutti i risultati della query e li salvo nella variabile "esami"

    conn.close() # Chiudo la connessione al database

    if not esami: # Controllo se la lista esami è vuota
        print("Nessun esame trovato nel piano di studio.") # Messaggio se non ci sono esami
        return # Esco dalla funzione
    
    for esame in esami: # Ciclo iterativamente su ogni esame nella lista esami
        # Valori nella tupla nel databse : esame [0] = id, esame [1] = nome, esame [2] = data_scadenza, esame [3] = cfu, esame [4] = paragrafi_totali, esame [5] = paraggrafi_studati 
        print(f"ID: {esame[0]} | Nome: {esame[1]} | Data: {esame[2]} | CFU: {esame[3]} | Paragrafi totali: {esame[4]} | Paragarfi già studiati: {esame[5]}") # Stampo i dettagli di ogni esame

# FUNZIONE : ELIMINA
def elimina_esame(): # Crea la funzione per eliminare un esame
    visualizza_esami() #Prima richiamo la funzione per visualizzare tutti gli esami presenti nel database per farli visualizzare all'utente
    print("\n--- Elimina un esame ---") # Stampa l'intestazione della sezione

    try: # Il try serve per gestire eventuali errori durante l'esecuzione del codice quindi provo a eseguire il codice seguente
        esame_da_eliminare = input("Quale esame vuoi eliminare?") # Chiedo all'utente di inseire il nome dell'esame e lo salvo"))
        conn = sqlite3.connect('study_planner.db') # Mi collego al database esistente
        cursore = conn.cursor() # Creo un cursore per eseguire i comandi SQL
        
        # Ceroc gli esami con quel nome
        cursore.execute('SELECT * FROM esami WHERE nome = ?', (esame_da_eliminare,)) # Faccio scorrere il cursore per cercare l'esame il nome inserito dall'utente, dopo la virgola serve per indicare che è una tupla con un solo elemento ('esame_da eleiminare)
        esami_trovati = cursore.fetchall() # Recupero tutti i risultati della query e li salvo nella variabile "esami_trovati"

        if not esami_trovati: # Controllo se la lista esami_trovati è vuota
            print(f"Nessun esame trovato conil nome '{esame_da_eliminare}'.") # Messaggio se non ci sono esami con quel nome
            return # Eesco dalla funzione
        
        if len(esami_trovati) == 1: #Controllo se c'è un solo esame con quel nome, len serve a restituire  la lungheza della lista e quindi capire se è uguale ad 1
            cursore.execute('DELETE FROM esami WHERE nome = ?', (esame_da_eliminare,)) # Eseguo il comando SQL per eliminare l'esame con quel nome
            print(f"L'esame '{esame_da_eliminare}' è stato eliminato con successo.") # Messaggio di conferma

        else: # Se ci sono più esami con quel nome
            print(f"Sono presenti più esami con il nome '{esame_da_eliminare}'.")
            for esame in esami_trovati: # Ciclo iterativamente su ogni esame nella lista esami_trovati
                print(f"ID: {esame[0]} | Nome: {esame[1]} | Data: {esame[2]} | CFU: {esame[3]} | Pragrafi totali: {esame[4]} | Paragrafi già studiati: {esame[5]}") # Stampo i dettagli di ogni esame trovato

            esame_id = int(input("Indica qui l'ID che corrisponde all'esame che vuoi eliminare: ")) # Chiedo all'utente di inserire l'ID dell'esame da eliminare e lo salvo come intero
            cursore.execute('DELETE FROM esami WHERE id = ?', (esame_id,)) # Eseguo il comando SQL per eliminare l'esame con quell'ID
            print(f"L'esame con ID '{esame_id}' è stato eliminato con successo.") # Messaggio di conferma

        conn.close() # Chiudo la connessione al database
    except ValueError: # Se si verifica un errore di tipo ValueError (ad esempio, l'utente inserisce un valore non valido)
        print(f"ID '{esame_id}' non valido. Potresti aver inserito un carattere sbagliato, un segno di punteggiatura o uno spazio che rende l'ID non corretto.") # Messaggio di errore    

if __name__ == "__main__" : # Eseguo la funzione solo se il file viene eseguito direttamente
    aggiungi_esame() # Chiamo la funzione per aggiungere un esame   