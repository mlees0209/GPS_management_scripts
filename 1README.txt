1README

This folder is a repository for all the GPS data I use. It contains UNAVCO data and NGL data. There are scripts which pull UNAVCO/PBO data automatically, and also one which pulls NGL data automatically.

Within each folder, the naming scheme is as follows:
STNNAME.DATASOURCE.REF_FRAME.FILEFORMAT

STNNAME is a 4 digit code eg P540 or CRCN
DATASOURCE is either ngl or pbo, depending on where the data was downloaded from. Some stations will have both datasources; others only one.
REF_FRAME is a code contianing the reference frame, eg "igs14' which is the centre of the earth or "na" which is north american.
FILEFORMAT is a bit weird, I don't quite understand, but they are really all delimited text files. 'csv' is obvious, 'tenv3' is less obvious but it's just a delimited text file.

There are also lists of station names in this folder, eg 'GPS_stations_CV.txt'. Why? You can use the fetch scripts to update multiple stations at once if you do: "fetch_GPS_data.sh" script. To do many files at once, try making a file with each station on a line and then doing: " cat file.txt | while read line; do ./fetch_GPS_data.sh $line; done".

