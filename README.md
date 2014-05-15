TwistedRPiCam
=============

Install
-------

```
sudo apt-get install python-twisted python-picamera python-rpi.gpio ssl-cert
adduser pi ssl-cert
```

Relogin to get access to ssl-cert group owned SSL key.

```
git clone https://github.com/esyscoder/TwistedRPiCam.git
```

Run
---

```
cd TwistedRPiCam
mkdir -p log
echo "admin:admin" > passwd 
./run_bg.sh
```

Use
---

Auto refreshing image:
```
http://<RPI.IP>:8080/
https://<RPI.IP>:8443/
```

One shot image:
```
http://<RPI.IP>:8080/cam.jpeg
https://<RPI.IP>:8443/cam.jpeg
```

TODO
----

- Configuration file
- Debian PPA package

LICENSE
-------

    TwistedRPiCam
    Copyright (C) 2014 ESYSCODER Dariusz Bączkowski

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

