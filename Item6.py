import requests
import netmiko
import json
from netmiko import ConnectHandler

cisco1 = {
    "ip": "192.168.2.104",
    "device_type": "cisco_ios",
    "username": "cisco",
    "password": "cisco123!",
}

# Mensaje de bienvenida
print("Bienvenido al programa de visualización de configuraciones de router CSR1000v")

print("¿Desea visualizar la configuración activa en la RAM?: ")
print("1 = Sí")
print("2 = No")
pregunta1 = str(input(""))
if pregunta1 =="1":
    # Show command that we execute.
    command = "show run"
    with ConnectHandler(**cisco1) as net_connect:
        output = net_connect.send_command(command)

    # Automatically cleans-up the output so that only the show output is returned
    print()
    print(output)
    print()

elif pregunta1 =="2":
    print("¿Desea visualizar la configuración de interfaces y direccionamiento IP?: ")
    print("1 = Sí")
    print("2 = No")
    pregunta2 = str(input(""))

    if pregunta2 =="1":
        # Comando show para revisar interfaces y direccionamiento IP.
        command2 = "show ip int br"
        with ConnectHandler(**cisco1) as net_connect:
            output2 = net_connect.send_command(command2)
        
        # Mostrar información de int/IP
        print()
        print(output2)
        print()
    
    elif pregunta2 =="2":
        print("¿Desea visualizar la información de la versión de IOS que se usa actualmente?: ")
        print("1 = Sí")
        print("2 = No")
        pregunta3 = str(input(""))

        if pregunta3 =="1":
            # Comando show para revisar versión de IOS.
            command3 = "show version"
            with ConnectHandler(**cisco1) as net_connect:
                output3 = net_connect.send_command(command3)
        
            # Mostrar información de int/IP
            print()
            print(output3)
            print()
        
        elif pregunta3 =="2":
            print("Gracias por su tiempo")
        
        else:
            print("Por favor, escriba sólo '1' o '2'")
    else:
        print("Por favor, escriba sólo '1' o '2'")
else:
    print("Por favor, escriba sólo '1' o '2'")