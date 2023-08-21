
import string
from netmiko import ConnectHandler
import getpass

class deviceCiscoModel:
    """Instantiate a Cisco Device to be manipulated"""
    numQuantitySwitchports=48  #Assumes a full size Cisco Switch model

    deviceType="cisco_ios"
    hostIP='192.168.3.20'
    loginUsername='admin'
    loginPassword='mehaw1'
    loginSecret='mehaw1!'
    netPortNum='22'

    consoleOutput="empty"


    def __init__(self):
        self.numQuantitySwitchports=48  #Assumes a full size Cisco Switch model

        self.deviceType="cisco_ios"
        self.hostIP='192.168.3.20'
        self.loginUsername='admin'
        self.loginPassword='mehaw1'
        self.loginSecret='mehaw1'
        self.netPortNum='22'


    def setQuantitySwitchPorts(self,qty):
        #self.numSwitchPorts = int(qty)
        self.numQuantitySwitchports=qty

    def setDeviceType(self,DeviceType):
        self.deviceType=DeviceType

    def setHostIP(self,IPAddr):
        self.hostIP=IPAddr

    def setLoginUsername(self,username):
        self.loginUsername=username

    def setLoginPassword(self,password):
        self.loginPassword=password

    def setLoginSecret(self,secret):
        self.loginSecret=secret

    def setNetPortNum(self,networkPort):
        self.netPortNum=networkPort

    def getQuantitySwitchPorts(self):
        return self.numQuantitySwitchports

    def getDeviceType(self):
        return self.deviceType

    def getHostIP(self):
        return self.hostIP

    def getLoginUsername(self):
        return self.loginUsername

    def getLoginPassword(self):
        return self.loginPassword

    def getLoginSecret(self):
        return self.loginSecret

    def getComPortNum(self):
        return self.netPortNum

    def deviceShowIPARP(self):
        # password = getpass.getpass() # for CLI
        #passwordLocal = password
        #targetDevice = deviceCiscoModel_Object

        login_info = {
            'device_type': self.getDeviceType(self),
            'host':   self.getHostIP(self),
            'username': self.getLoginUsername(self),
            'password': self.getLoginPassword(self)
        }

        net_connect = ConnectHandler(**login_info)

        s = net_connect.send_command('show ip arp')

        net_connect.disconnect()

        print(s)
        self.consoleOutput=s

    def showOutput(self):
        return(self.consoleOutput)








