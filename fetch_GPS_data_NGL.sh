#!/bin/bash

# Takes input of a GPS station name (eg P571) and updates the NGL downloaded files for that station.

stationname=$1

mkdir -p $stationname

# NOT QUITE FINISHED BUT THIS ALMOST WORKS; DOES IT CHECK FOR NEW AT THE REMOTE END?!
wget -np -nH --cut-dirs=3 --reject="index.html*" http://geodesy.unr.edu/gps_timeseries/tenv3/IGS14/$stationname.tenv3 -O $stationname/$stationname.ngl.igs84.tenv3
wget -np -nH --cut-dirs=3 --reject="index.html*" http://geodesy.unr.edu/gps_timeseries/tenv3/plates/NA/$stationname.NA.tenv3 -O $stationname/$stationname.ngl.na.tenv3


