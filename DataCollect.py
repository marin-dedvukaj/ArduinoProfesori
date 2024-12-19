import serial.tools.list_ports
import serial
import time

class Reciver():

    # Connect to arduino
    def arduinoConnect(self):
        baudRate = 9600
        self.arduinoPort = None
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if "Arduino" in port.description or "Arduino" in port.manufacturer:
                self.arduino_port = port.device
                break

        if not self.arduinoPort:
            print("No Arduino found.")
        self.ser = serial.Serial(self.arduino_port,self.baudRate,timeout=10)
        time.sleep(2)
        return None
    
    # Connect to the arduino on cleass init 
    def __init__(self):
        self.arduinoConnect()

        pass

    # Receive data from arduino connection
    def receive(self):
        try:
            data = self.ser.readline().decode("utf-8").strip().split("/")
            pass
        except Exception as exc:
            print(exc)
            self.arduinoConnect()

        return data


#run func if file is excecuted directly 
def main():
    rec = Reciver()
    print("starting reading")
    while True:
        try:
            print(rec.receive())
        except KeyboardInterrupt:
            print("Ending reading....")

    return None 

if __name__ == "__main__":
    main()
