import http.client

listaVerbi=['OPTIONS','PUT','HEAD','DELETE','TRACE','CONNECT','GET','POST']

host = input("Inserire l'IP del sistema target: ")
port = input("Inserire la porta del sistema target (default '80'): ")
path = input("Inserire il path di cui si vuole avere una lista dei metodi abilitati (default '/'): ")

try:
    connection = http.client.HTTPConnection(host, port)
    for i in listaVerbi:
        connection.request(i,path)
        response=connection.getresponse()

        if(response.status == 200):
            print("Il metodo " + i + " è abilitato.")

        connection.close()
except ConnectionRefusedError:
    print("Connessione fallita")
