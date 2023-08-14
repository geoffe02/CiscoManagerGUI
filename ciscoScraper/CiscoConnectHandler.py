
#Code snippet for trying out.  Delete file later.

from netmiko import ConnectHandler
import getpass


password = getpass.getpass() 

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