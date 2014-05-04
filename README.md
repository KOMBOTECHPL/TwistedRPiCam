TwistedRPiCam
=============

Install
-------

```
sudo apt-get install python-twisted python-picamera python-rpi.gpio
git clone https://github.com/esyscoder/TwistedRPiCam.git
```

Run
---

```
cd TwistedRPiCam
mkdir -p log
./run_bg.sh
```

Use
---

Auto refreshing image:
```
http://<RPI.IP>:8080/
```

One shot image:
```
http://<RPI.IP>:8080/cam.jpeg
```

TODO
----

- Digest authentication
- Configuration file
- Debian PPA package
