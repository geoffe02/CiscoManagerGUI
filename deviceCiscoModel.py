import string

class deviceCiscoModel:
    """Instantiate a Cisco Device to be manipulated"""

    def __init__(self):
        self.numQuantitySwitchports=48  #Assumes a full size Cisco Switch model

        self.deviceType="cisco_ios"
        self.hostIP='192.168.1.1'
        self.loginUsername='admin'
        self.loginPassword='admin'
        self.loginSecret='admin'
        self.netPortNum='22'


    def setQuantitySwitchPorts(self, qty):
        numSwitchPorts = int(qty)
        self.numQuantitySwitchports=numSwitchPorts

    def setDeviceType(self, DeviceType):
        self.deviceType=DeviceType

    def setHostIP(self, IPAddr):
        self.hostIP=IPAddr

    def setLoginUsername(self, username):
        self.loginUsername=username

    def setLoginPassword(self, password):
        self.loginPassword=password

    def setLoginSecret(self, secret):
        self.loginSecret=secret

    def setNetPortNum(self, networkPort):
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







