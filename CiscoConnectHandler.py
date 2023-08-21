
#Code snippet for trying out.  Delete file later.

# from ssl import _PasswordType
from netmiko import ConnectHandler
import getpass
import deviceCiscoModel

def deviceConnect(deviceCiscoModel_Object):
    # password = getpass.getpass() # for CLI
    #passwordLocal = password
    targetDevice = deviceCiscoModel_Object

    login_info = {
        'device_type': targetDevice.getDeviceType(),
        'host':   targetDevice.getHostIP(),
        'username': targetDevice.getLoginUsername(),
        'password': targetDevice.getLoginPassword()
    }

    net_connect = ConnectHandler(**login_info)

    s = net_connect.send_command('show ip arp')

    net_connect.disconnect()

    print(s)
    return(s)