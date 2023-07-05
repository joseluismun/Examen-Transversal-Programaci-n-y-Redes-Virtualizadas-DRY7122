from ncclient import manager

router_ip = "192.168.56.106"  # Reemplaza con la dirección IP del router CSR1000v
router_username = "cisco"  # Reemplaza con el nombre de usuario para SSH en el router
router_password = "cisco123!"  # Reemplaza con la contraseña para SSH en el router

def connect_to_router():
    return manager.connect(
        host="192.168.56.106",
        port=830,
        username="cisco",
        password="cisco123!",
        device_params={'name': 'csr'}
    )

with connect_to_router() as m:
    # Aquí puedes realizar operaciones NETCONF utilizando el objeto 'm'
    # Por ejemplo, obtener información del router
    result = m.get_config(source='running').data_xml
    print(result)