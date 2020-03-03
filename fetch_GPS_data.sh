#!/bin/bash

# Takes input of a GPS station name (eg P571) and updates the UNAVCO downloaded files for that station.

stationname=$1

export PATH=$PATH:/usr/local/bin/wget

wget -r -np -nH --cut-dirs=3 --reject="index.html*" -N  -P . ftp://data-out.unavco.org/pub/products/position/$stationname
