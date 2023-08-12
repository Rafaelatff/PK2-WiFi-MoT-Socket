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


  




