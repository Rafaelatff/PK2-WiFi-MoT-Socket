# PK2-WiFi-MoT-Socket
More studies.

## Adding files to git

Create the repositorie on GitHub (using browser). In the explorer, inside the project folder, go to git bash here.

Then use: 
```
$ git init
$ git remote add origin https://github.com/Rafaelatff/PK2-WiFi-MoT-Socket.git
$ git add .
$ git commit -m "adding initial files"
$ git push --set-upstream origin master
```

Then we will create a new branch, so we can work without worries with the original files.

```
$ git checkout -b learning
$ git push --set-upstream origin learning

```

## Let's test

To test the current code, FIRMWARE SIDE:

* Go to folder _0_MoT_WiFi_RSSI_PSR and open the file _0_MoT_WiFi_RSSI_PSR.ino.
* Then comment previous SSID and Password, and add (or uncomment) the current one.

![image](https://github.com/Rafaelatff/PK2-WiFi-MoT-Socket/assets/58916022/d8437e84-c334-445e-86c9-44aa33d0c7d7)

* Then select the COMx and the board NodeMCU 1.0 (ESP-12E Module).
* Then open the termial at a 115200 baud.

SOFTWARE SIDE:

* Open the N3_Python_RSSI_PSR.py code and run it.
* Type the PK2 IP.

Serial didn't print the PK2 IP, then I checked on the router.

![image](https://github.com/Rafaelatff/PK2-WiFi-MoT-Socket/assets/58916022/6b2de3a9-6f06-489e-9d07-adf72d1b7408)

* Type the port.
* Type the number of measurements.

![image](https://github.com/Rafaelatff/PK2-WiFi-MoT-Socket/assets/58916022/b93ed464-9664-4ba4-9709-8d5b600c541f)

* Then open the N6_Python_Exibi_RSSI_PSR.py code.
* I had to install schedule. At the terminal I typed: 'pip3 install schedule'.

![image](https://github.com/Rafaelatff/PK2-WiFi-MoT-Socket/assets/58916022/668f50a6-f217-4958-8327-d55e1739415f)

## Statistics over the data

Now that I have the fluxogram and the codes running, I will implement some statiscs over the collected data. First of all, I will implement a new python, that can calculate the mean, the standard deviation and also plot a histogram. Some help for this process can be found [here](https://github.com/Rafaelatff/DataCamp-Intermediate-Python/tree/main).

The generated files stays at location "PK2-WiFi-MoT-Socket\Pythons" and are named "Medidas_YYYY_MM_DD_HH-mm-ss.txt" where: **YYYY** stands for the year, **MM** month, **DD** day, **HH** hour, **mm** minute and **ss** for the second of the recorded data (moment of creation of the file).

To read the data, I had to ignorate the first row (```skiprows=1```) and also the last row (```.readlines()[:-1]```).

```py
RSSIdl = np.loadtxt(open("Medidas_2022_02_03_09-57-35.txt", mode='r').readlines()[:-1], skiprows=1, delimiter=';', usecols=[3])
```

Then I plot the data:

```py
plt.figure(1)
plt.subplot(2,2,1) 
plt.plot(RSSIdl) 
plt.xlabel('Time domain') 
plt.ylabel('RSSI') 
plt.title('RSSI DL 2022 - 1322 RSSIs')

plt.subplot(2,2,2)
plt.hist(RSSIdl, bins=20)
```

And calculate the mean and the standard deviation:

```py
print('Mean: ' + str(np.float64(np.mean(RSSIdl)))) # It returns a <numpy.float64> type, then is converted to string
print('Standard deviation: ' + str(np.float64(np.std(RSSIdl)))) # Same as before
```

I had as results, for two logs: 

![image](https://github.com/Rafaelatff/PK2-WiFi-MoT-Socket/assets/58916022/96c65ccc-a7a7-45db-be5d-cf6c1a20eb9d)

* Mean: 6.866598639455782
* Standard deviation: 6.826359900338357

![image](https://github.com/Rafaelatff/PK2-WiFi-MoT-Socket/assets/58916022/205444c5-e23a-452a-b117-7f7163496f3a)

* Mean: 73.26285896454986
* Standard deviation: 11.83503385862668

None of them with a normal distribution. Lets try to collect more data and try again tomorrow! 
Now with 100000 of data: 

![WhatsApp Image 2023-09-13 at 12 07 35](https://github.com/Rafaelatff/PK2-WiFi-MoT-Socket/assets/58916022/80931b84-2fa7-4d4f-b91d-c765ec2bbbce)

* Mean: -52.034114434876535
* Standard deviation: 2.757370986817883

I had some troubles by recovering the data, original file just save first tree rows (see next image). Previews data were copied from the terminal, pasted on a excel sheet, then I converted text to column, deleted all the non usable lines, then I copied again to a txt file. This took a lot of time! So, before going to the running statistics, I will study the python giles that generate de txt data with the measurements.

![image](https://github.com/Rafaelatff/PK2-WiFi-MoT-Socket/assets/58916022/593d7e61-0773-46ee-bc98-17962f9c1a06)

## N3_Python_RSSI_PSR.py

### Socket configuration

```py
import socket # To use [socket.py](https://docs.python.org/3/library/socket.html) lib.
# This module provides access to the BSD socket interface. It is available on all modern Unix systems, Windows, MacOS, and probably additional platforms.
# It is a programming interface and API (Application Programming Interface) for network communication.

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Creates a object named "udp" and configure it as IPv4 address family and UDP protocol.
udp.settimeout(0.5) # Set 0.5 seconds as timeout
```

* ```socket.AF_INET``` - is a constant that indicates the address family that will be used. In this case, AF_INET refers to the IPv4 address family.
* ```socket.SOCK_DGRAM``` - is a constant that indicates the type of socket that will be created. In this case, SOCK_DGRAM indicates that it will be a datagram type socket, used for communication based on the UDP protocol.
* ```.settimeout()``` It is a method of the socket class (socket) which sets a timeout (in seconds) for socket I/O operations. This is useful to prevent the program from blocking indefinitely during a receive operation.
* It must finish with a ```udp.close()```.

```py
HOST = input("Digite o endereco IP do sensor:")  # Now I have to type (on CLI/terminal), the IP that my router assigned to the PK2 board.
PORT = input("Digite A porta do Socket:") # And then I type the socket door that PK2 is connected.
HOST2 = ''  #endereço do Servidor socket

Sensor = (HOST, int(PORT))   #conjunto endereço e porta utilizado para o envio da informação
orig = (HOST2, int(PORT))     ##conjunto endereço e porta utilizado para o recebimento da informação

```

```py
udp.bind(orig) #  Inicializa o socket de escuta
```


## Running statistics

In previous studies, I prepared some code to run the running statistics over random generated data with normal distribution and then using the IZ data (studies for the [WissTek](http://www.wisstek.org) Lab). More information can be found [here](https://github.com/Rafaelatff/Running-statistics).

[TBC] - Then I will apply some running statistics over the data.
  




