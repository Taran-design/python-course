from abc import ABC, abstractmethod

class SmartDevice(ABC):
    @abstractmethod
    def command(self):
        pass
    
class SmartLight(SmartDevice):
    def command(self):
        print("Smart light: Turning on lights")

class SmartSpeaker(SmartDevice):
    def command(self):
        print("Smart speaker: Turning on the lights")

class SmartThermostat(SmartDevice):
    def command(self):
        print("Smart thermostat: Adjusting temperature")

light = SmartLight()
speaker = SmartSpeaker()
thermostat = SmartThermostat()

devices = [light, speaker, thermostat]
for device in devices:
    device.command()