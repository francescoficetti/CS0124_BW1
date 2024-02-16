import http.client  #Import del modulo http.client

listaVerbi=['OPTIONS','PUT','HEAD','DELETE','TRACE','CONNECT','GET','POST'] #Lista di verbi HTTP

host = input("Inserire l'IP del sistema target: ")
port = input("Inserire la porta del sistema target (default '80'): ")
path = input("Inserire il path di cui si vuole avere una lista dei metodi abilitati (default '/'): ")

if (port == "" or int(port) <0 or int(port) >65535): #Se l'utente non inserisce la porta corretta, viene impostata di default la porta 80.
    print("E' stata impostata la porta di default.\n")
    port=80

if (path == ""): #Se l'utente non inserisce il path, viene impostato di default il path '/'.
    print("E' stato impostato il path di default.\n")
    path="/"

try:
    connection = http.client.HTTPConnection(host, port) #Viene instaurata una connessione con la macchina target.
    for i in listaVerbi:
        connection.request(i,path) #Invio di una richiesta HTTP per ogni verbo della lista.
        response=connection.getresponse() #Ricezione della risposta dal server

        if(response.status == 200): #Se il metodo getresponse() ha restituito come valore "200", la connessione è andata a buon fine. 
            print("Il metodo " + i + " è abilitato.")

        connection.close() #Chiusura della connessione
except ConnectionRefusedError: #Gestione dell'errore "ConnectionRefused"
    print("Connessione fallita")
