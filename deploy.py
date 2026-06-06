from netmiko import ConnectHandler
from devices import infrastructure

def deploy_by_name(target_name):
    #Verifica de existencia del dispositivo
    if target_name not in infrastructure:
        print(f"[!] Device {target_name} does not exist")
        return

    #Carga de datos del equipo y archivo de configuración
    device_data = infrastructure[target_name]
    route_cfg = f"configs/{target_name}.cfg"

    print(f"\n[+] Deploy started in: {target_name}")    
    try:
        #Establecimiento de la conexión SSH
        conexion = ConnectHandler(**device_data)
        print(f"    Deployment in: {route_cfg}")
        
        #Lectura del archivo .cfg e inyección de comandos
        conexion.send_config_from_file(route_cfg)
        
        #Guardado de configuración y cierre de sesión SSH
        conexion.save_config()
        conexion.disconnect()
        
        print(f"    [OK] {target_name} updated.")
        
    except Exception as e:
        print(f"    [ERROR] {target_name} fail: {e}")

#Ejecución de la función
deploy_by_name("R1")