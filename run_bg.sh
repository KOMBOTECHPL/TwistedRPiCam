#!/bin/bash

export PYTHONPATH=`pwd`
/usr/bin/twistd --pidfile=TwistedRPiCam.pid --logger TwistedRPiCam.tlog.logger -y trun.py
