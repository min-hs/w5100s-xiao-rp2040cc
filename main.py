from usocket import socket
from machine import Pin, SPI, ADC
import network
import time
import neopixel
import _thread

np = neopixel.NeoPixel(machine.Pin(12), 1)
p0 = Pin(11, Pin.OUT)
p0.off()

# W5x00 chip initialization
def w5x00_init():
    spi = SPI(0, 2_000_000, mosi=Pin(3), miso=Pin(4), sck=Pin(2))
    nic = network.WIZNET5K(spi, Pin(1), Pin(0))  # spi, cs, reset pin
    nic.active(True)

    # None DHCP
    nic.ifconfig(('192.168.11.20', '255.255.255.0', '192.168.11.1', '8.8.8.8'))

    # DHCP
    # nic.ifconfig('dhcp')
    print('IP address:', nic.ifconfig())
    
    p0.on()

    while not nic.isconnected():
        time.sleep(1)
        #print(nic.regs())

def server_loop(): 
    s = socket()
    s.bind(('192.168.11.20', 5000)) #Source IP Address
    s.listen(5)
    
    print("TEST server")
    conn, addr = s.accept()
    print("Connect to:", conn, "address:", addr) 
    print("Loopback server Open!")
    _thread.start_new_thread(led_status_func, ())
    while True:
        data = conn.recv(2048)
        print(data.decode('utf-8'))
        if data != 'NULL':
            conn.send(data)

def client_loop():
    s = socket()
    s.connect(('192.168.11.74', 5000)) #Destination IP Address
    
    print("Loopback client Connect!")
    _thread.start_new_thread(led_status_func, ())
    while True:
        data = s.recv(2048)
        print(data.decode('utf-8'))
        if data != 'NULL' :
            s.send(data)

def led_status_func():
    while True:
        np[0] = (255,0,0)
        np.write()
        time.sleep(0.2)
        np[0] = (0,255,0)
        np.write()
        time.sleep(0.2)
        np[0] = (0,0,255)
        np.write()
        time.sleep(0.2)
        
def main():
    w5x00_init()
    
    
###TCP SERVER###
    server_loop()

###TCP CLIENT###
    #client_loop()

if __name__ == "__main__":
    main()
