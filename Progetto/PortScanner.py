import socket

open_port = {}
lower_port, higher_port = 0, 65535

target_ip = input("Inserisci l'indirizzo ip per la scansione delle porte: ")

scanner = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for port in range(lower_port, higher_port+1):
    try:
        if(scanner.connect_ex((target_ip, port)) == 0):
            open_port[port] = "Aperta", socket.getservbyport(port, 'udp')
        else:
            open_port[port] = "Chiusa"
    except OSError:
        open_port[port] = "Chiusa"
        continue
scanner.close()

print("\nIl prospetto delle porte UDP è:", open_port)