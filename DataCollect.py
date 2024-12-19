import serial.tools.list_ports
import serial
import time

class Reciver():

    #connect to arduino
    def arduinoConnect(self):
        baudRate = 9600
        #set a variable that contains port where arduino is tored to None 
        self.arduinoPort = None
        #collect all ports scanned to a variable 
        ports = serial.tools.list_ports.comports()
        #iterate through ports to find the one connected to arduino
        for port in ports:
            if "Arduino" in port.description or "Arduino" in port.manufacturer:
                #add arduino port to the variable and then 
                self.arduino_port = port.device
                break
        #check if arduino was found or not 
        if not self.arduinoPort:
            print("No Arduino found.")
        #inicialize connection with arduino and wait it to be properly established before returning
        self.ser = serial.Serial(self.arduino_port,self.baudRate,timeout=10)
        time.sleep(2)
        return None
    
    #connect to the arduino on cleass init 
    def __init__(self):
        self.arduinoConnect()

        pass

    #recive data from arduino connection
    def receive(self):
        try:
            #recive data, decode for special characters, removewhitespace, split at the / to obtain a list of the diferent data
            data = self.ser.readline().decode("utf-8").strip().split("/")
            pass
        except Exception as exc:
            #if we encounter error dael with it in case of arduino not connected reconnect
            print(exc)
            self.arduinoConnect()

        return data


#run func if file is excecuted directly 
def main():
    #inicialize class
    rec = Reciver()
    print("starting reading")
    #loop to recive data and print untill ctr + c is pressed 
    while True:
        try:
            print(rec.receive())
        except KeyboardInterrupt:
            print("Ending reading....")

    return None 

if __name__ == "__main__":
    main()
