import serial.tools.list_ports
import serial
import time

class Reciver():
    
    def __init__(self):
        self.portScanner()
        self.baudRate = 9600
        pass

    #scann the ports on the computer and 
    def portScanner(self):
        self.arduinoPort = None
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if "Arduino" in port.description or "Arduino" in port.manufacturer:
                self.arduino_port = port.device
                return None
        if not self.arduinoPort:
            print("No Arduino found.")
        self.ser = serial.Serial(self.arduino_port,self.baudRate,timeout=10)
        time.sleep(2)
        return None

    def receive(self):
        try:
            data = self.ser.readline().decode("utf-8").strip().split("/")
            pass
        except Exception as exc:
            print(exc)
            self.portScanner()

        return data

def main():
    rec = Reciver()
    print("starting reading")
    while True:
        try:
            print(rec.receive())
        except KeyboardInterrupt:
            print("Ending reading....")
    
    return

if __name__ == "__main__":
    main()
