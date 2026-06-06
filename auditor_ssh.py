from netmiko import ConnectHandler

router_cisco = {
    'device_type': 'cisco_ios',
    'host':   '192.168.68.134',
    'username': 'hector',
    'password': 'cisco',
    'port': 1022,
}

print(f"Iniciando conexión SSH hacia {router_cisco['host']}...")

try:
    #Establecimiento de la conexión SSH
    conexion = ConnectHandler(**router_cisco)
    print("¡Conexión exitosa! Sesión establecida.\n")

    #Envio de comando de lectura y guardado de respuesta
    comando = "show ip interface brief"
    print(f"Ejecutando comando: '{comando}'...\n")
    salida_comando = conexion.send_command(comando)

    #Impresión de respuesta del router en consola
    print("--- RESULTADO ---")
    print(salida_comando)
    print("-----------------\n")

    #Cierre de la conexión SSH
    conexion.disconnect()
    print("Sesión SSH cerrada correctamente.")

except Exception as error:
    print(f"Ocurrió un error al intentar conectar: {error}")