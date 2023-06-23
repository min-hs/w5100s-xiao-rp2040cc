```
Once you have your XIAO-RP2040 and W5100S Ethernet module mounted, as shown in the figure below, you are ready to get started.
```

![<W5100S-XIAO> <XIAO-RP2040> <W5100S-XIAO + XIAO-RP2040>](https://hackster.imgix.net/uploads/attachments/1603479/image_mLFFqRReOu.png?auto=compress%2Cformat&w=740&h=555&fit=max)

<W5100S-XIAO> <XIAO-RP2040> <W5100S-XIAO + XIAO-RP2040>



Now let's set up Micropython in our environment. *Connect Raspberry Pi Pico to desktop or laptop using 5 pin micro USB cable.*

### Development environment configuration

![img](https://hackster.imgix.net/uploads/attachments/1603483/image_T8qmrGvq5B.png?auto=compress%2Cformat&w=740&h=555&fit=max)

**MicroPython Thonny IDE**

Install `Thonny IDE` on Raspberry Pi Pico by referring to the link

Thonny IDE Link : [Thonny](https://thonny.org/)



1. The drive will be called **RPI-RP2** on all RP2040 boards. Download the **UF2**(rp2_w5100s_20221111_v2.0.0.uf2) file from the link below and put the file in Pico.

F/W Download link : [W5100S-XIAO-RP2040](https://github.com/Wiznet/RP2040-HAT-MicroPython/releases/download/v2.0.0/rp2_w5100s_20221111_v2.0.0.uf2)



2. You can also access the firmware installation menu if you click on **MicroPython (Raspberry Pi Pico)** in the status bar and choose ‘Configure interpreter …’.

![img](https://hackster.imgix.net/uploads/attachments/1603484/image_KwJ5NzFq6K.png?auto=compress%2Cformat&w=740&h=555&fit=max)



3. Look at the Shell panel at the bottom of the "Thonny" editor. You should see something like this:

![img](https://hackster.imgix.net/uploads/attachments/1603485/image_eDQIR0G76k.png?auto=compress%2Cformat&w=740&h=555&fit=max)

### Ethernet Test

Now that we're done setting up our environment, let's implement TCP/IP Ethernet.

Import the Ethernet source from the link below, which is a basic TCP/IP send/receive example from the Loopback sample.

[https://github.com/min-hs/w5100s-xiao-rp2040.git](https://github.com/min-hs/w5100s-xiao-rp2040cc.git)

![enable Server ](https://hackster.imgix.net/uploads/attachments/1604542/image_4wwontHIF7.png?auto=compress%2Cformat&w=740&h=555&fit=max)

enable Server

Since the W5100S-XIAO board will be acting as a server, enable the **server_loop()** function and run the code to wait for the client to connect. When you run the code, the IP address information appears as shown below.

![img](https://hackster.imgix.net/uploads/attachments/1604543/image_6DoaxrbGSe.png?auto=compress%2Cformat&w=740&h=555&fit=max)

When a client connects, an RGB LED lights up on the board.

![img](https://hackster.imgix.net/uploads/attachments/1604569/image_XKAC7h8jsv.png?auto=compress%2Cformat&w=740&h=555&fit=max)



![img](https://hackster.imgix.net/uploads/attachments/1604570/image_TgX2sWzTpD.png?auto=compress%2Cformat&w=740&h=555&fit=max)