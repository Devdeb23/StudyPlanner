import sqlite3 #Importo la libreria per parlare con il database

def crea_tabelle():
    # Definisco la funzione per collgarmi dierettamente al database

    conn = sqlite3.connect('study_planner.db') #Mi collego al database (se non esiste lo crea)

    cursore = conn.cursor() #Creo un cursore per eseguire i comandi SQL
    # Inserisco IF NOT EXISTS per evitare errori nel caso la tabella esista già
    cursore.execute(''' 
                    CREATE TABLE IF NOT EXISTS esami ( 
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nome TEXT NOT NULL, 
                    data_scadenza DATE NOT NULL, 
                    cfu INTEGER, 
                    paragrafi_totali INTEGER, 
                    paragrafi_studiati INTEGER DEFAULT 0 
                    )
                    ''') # Creo la tabella esami con i campi necessari
    
    conn.commit() # Salvo le modifiche

    conn.close() # Chiudo il collegamento al database 
    print("Database e tabella creati con successo!") # Messaggio di conferma

if __name__ == "__main__" : # Eseguo la funzione solo se il file viene eseguito direttamente
    crea_tabelle() # Chiamo la funzione per creare le tabelle
