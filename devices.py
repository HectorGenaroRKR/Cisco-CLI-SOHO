# Definimos credenciales globales para no reescribirlas
IP_GATEWAY = '192.168.68.134'
GLOBAL_USER = 'hector'
GLOBAL_PASSWORD = 'cisco'

infrastructure = {
    # Diccionario del Router
    "R1":{
        'device_type': 'cisco_ios',
        'host': IP_GATEWAY,
        'port': 1022,
        'username': GLOBAL_USER,
        'password': GLOBAL_PASSWORD,
    },

    # Diccionario del Switch
    "SW1":{
        'device_type': 'cisco_ios',
        'host': IP_GATEWAY,
        'port': 2022,
        'username': GLOBAL_USER,
        'password': GLOBAL_PASSWORD,
    }
}