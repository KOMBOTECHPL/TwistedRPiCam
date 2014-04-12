#!/bin/bash

PID=`cat TwistedRPiCam.pid 2>/dev/null`
if [ "$PID" = "" ]
then
  echo "No running server!"
else
  echo "Killing server: $PID!"
  kill $PID
  if true 
  then
    sleep 1
    echo "Force killing server: $PID!"
    kill -9 $PID
  fi
fi
