from ncclient import manager

router_ip = "192.168.56.106"  # Reemplaza con la dirección IP del router CSR1000v
router_username = "cisco"  # Reemplaza con el nombre de usuario para SSH en el router
router_password = "cisco123!"  # Reemplaza con la contraseña para SSH en el router

def change_router_name(new_name):
    netconf_payload = f'''
    <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <hostname>Josaphat_Munoz_Malhue_Sanchez</hostname>
        </native>
    </config>
    '''
    with manager.connect(
        host="192.168.56.106",
        port=830,
        username="cisco",
        password="cisco123!",
        hostkey_verify=False
    ) as m:
        result = m.edit_config(config=netconf_payload, target='running')
        print("Nombre del router cambiado con éxito.")

new_router_name = 'Josaphat_Munoz_Malhue_Sanchez'  # Reemplaza con el nuevo nombre para el router
change_router_name(new_router_name)