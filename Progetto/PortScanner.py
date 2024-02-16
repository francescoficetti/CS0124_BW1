import socket #Import del modulo socket per instaurare una connessione

def PortScanner(protocollo_socket, protocollo): #Definizione del metodo per il controllo delle porte
    scanner = socket.socket(socket.AF_INET, protocollo_socket) #Definizione del socket di tipo IPV4 e protocollo definito nella variabile
    for port in range(lower_port, higher_port+1): #Scansione delle porte in un intervallo specificato.
        try:
            if(scanner.connect_ex((target_ip, port)) == 0): #Verifica del tentativo di connessione verso l'ip target con la porta specificata
                open_port[port] = "Aperta", socket.getservbyport(port, protocollo) #Scrittura nel dizionario delle porte con il relativo stato ed eventualmente il protocollo
            else:
                open_port[port] = "Chiusa"
        except OSError: #Gestione dell'eccezione in caso dell'errore OSError
            open_port[port] = "Chiusa"
            continue
    scanner.close() #Chiusura del socket

#Inizio della funzione principale

#Dichiarazione degli oggetti
open_port = {}
lower_port, higher_port = -1, 65536

target_ip = input("Inserisci l'indirizzo IP della macchina target: ")

#Controllo della validità delle porte
while(lower_port < 0 or higher_port > 65535):
    lower_port = int(input("Inserisci la porta di partenza: "))
    higher_port = int(input("Inserisci l'ultima porta: "))

#Richiamo della funzione portscanner con socket in modalità UDP
PortScanner(socket.SOCK_DGRAM, 'udp')
print("\nIl prospetto delle porte UDP è:", open_port)

#Rimozione di tutti gli elementi dal dizionario
open_port.clear()

#Richiamo della funzione portscanner con socket in modalità TCP
PortScanner(socket.SOCK_STREAM, 'tcp')
print("\nIl prospetto delle porte TCP è:", open_port)
