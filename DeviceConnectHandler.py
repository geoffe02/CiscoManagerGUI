from netmiko import ConnectHandler
import getpass

class DeviceConnectHandler():
    """Handler for initial connection to Cisco Device"""

    def __init__(self):
        print ("Cisco device connect\n")
  

        password = getpass.getpass() #input password

        login_info = {
            'device_type': 'cisco_ios',
            'host':   '192.168.3.1',
            'username': 'admin',
            'password': password,
            }
        net_connect = ConnectHandler(**login_info)
        s = net_connect.send_command('show ip arp')
        net_connect.disconnect()
        print(s)

devLogin = DeviceConnectHandler()



