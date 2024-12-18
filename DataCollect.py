import serial.tools.list_ports
import serial
import time

class Reciver():
    
    def __init__(self):
        self.portScaner()
        self.baudRate = 9600
        pass

    
    def portScaner(self):
        self.arduinoPort = None
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if "Arduino" in port.description or "Arduino" in port.manufacturer:
                self.arduino_port = port.device
                return None
        if not self.arduinoPort:
            print("No Arduino found.")
        self.ser = serial.Serial(self.arduino_port,self.baudRate,timeout=10)
        return None

    def recive(self):
        try:
            pass
        except Exception as hi:
            print(hi)
            
        return

def main():
    print("hello world")
    rec = Reciver()
    print(rec.recive())
    return

if __name__ == "__main__":
    main()
