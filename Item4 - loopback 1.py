from ncclient import manager

IP_Router = "192.168.56.106"
username = "cisco"
password = "cisco123!"

netconf_manager = manager.connect(
    host="192.168.56.106",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
)

config = '''
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>Loopback1</name>
      <description>Loopback interface</description>
      <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
      <enabled>true</enabled>
      <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        <address>
          <ip>1.1.1.1</ip>
          <netmask>255.255.255.255</netmask>
        </address>
      </ipv4>
    </interface>
  </interfaces>
</config>
'''

response = netconf_manager.edit_config(target="running", config=config)
print(response)

netconf_manager.close_session()