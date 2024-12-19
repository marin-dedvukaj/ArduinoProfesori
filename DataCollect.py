import serial.tools.list_ports
import serial
import time

class Reciver():

    #connect to arduino
    def portScanner(self):
        #set a variable that contains port where arduino is tored to None 
        self.arduinoPort = None
        #collect all ports scanned to a variable 
        ports = serial.tools.list_ports.comports()
        #iterate through ports to find the one connected to arduino
        for port in ports:
            if "Arduino" in port.description or "Arduino" in port.manufacturer:
                #add arduino port to the variable and then 
                self.arduino_port = port.device
                pass
        if not self.arduinoPort:
            print("No Arduino found.")
        self.ser = serial.Serial(self.arduino_port,self.baudRate,timeout=10)
        time.sleep(2)
        return None
    

    def __init__(self):
        self.portScanner()
        self.baudRate = 9600
        pass


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
