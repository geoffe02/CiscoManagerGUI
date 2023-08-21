
#Code snippet for trying out.  Delete file later.

from ssl import _PasswordType
from netmiko import ConnectHandler
import getpass

def deviceConnect(password):
    # password = getpass.getpass() # for CLI
    passwordLocal = password

    login_info = {
        'device_type': 'cisco_ios',
        'host':   '192.168.3.1',
        'username': 'admin',
        'password': passwordLocal,
    }

    net_connect = ConnectHandler(**login_info)

    s = net_connect.send_command('show ip arp')

    net_connect.disconnect()

    print(s)
    return(s)