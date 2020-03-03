#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:41:04 2019

@author: mlees
"""

import sys
sys.path.append('/Users/mlees/Documents/RESEARCH/InSAR_processing/postprocessing_scripts')
sys.path.append('/home/mlees/InSAR_processing/postprocessing_scripts')

from InSAR_postSBAS import *
import seaborn as sns

stationslist = np.loadtxt('drummer1_repo/GPS_stations_CV_and_Sierras.txt',dtype='str')

plt.ioff()
plt.figure(figsize=(18,12))
sns.set_context('talk')

gpsstations = import_GPS_stations()

import simplekml
kml = simplekml.Kml()

# Do UNAVCO stations
for stn in stationslist:
    plot_individual_gps_station_vertical(stn,update=0)
    plt.savefig('GPSPLOTS/%s.jpg' % stn)
    plt.cla()
    logical=gpsstations['# ID']==stn
    
    
    kml.newpoint(name="%s" % stn,coords=[(gpsstations['Longitude'][logical].values[0],gpsstations['Latitude'][logical].values[0])],description='<img style="max-width:800px;" src="GPSPLOTS/%s.jpg">' % stn )

newstationslist = ['CAHA','CAWO','LIND','CRCN','LEMA','HELB','DONO','RAPT']

newstations = pd.read_csv('South_Central_valley_stations.csv')
#%%
# Do NGL stations
for stn in newstationslist:
    plot_individual_gps_station_vertical(stn,sln_type='ngl',update=0)
    plt.savefig('GPSPLOTS/%s_ngl.jpg' % stn)
    plt.cla()
    idx = np.argwhere(np.isin(newstations['Station_Name'],stn))[0]
    
    
    kml.newpoint(name="%s_ngl" % stn,coords=[(newstations['Lon'][idx].values[0],newstations['Lat'][idx].values[0])],description='<img style="max-width:800px;" src="GPSPLOTS/%s_ngl.jpg">' % stn )


kml.save("CentralValleyplus_Sierra_GPS_timeseries_NEW.kml")

cmd ='/Applications/MATLAB_R2018b.app/bin/matlab -nosplash -nodesktop -nodisplay -r "GIS_kml2kmz(\'CentralValleyplus_Sierra_GPS_timeseries_NEW.kml\')"'
cmd ='matlab -nosplash -nodesktop -nodisplay -r "GIS_kml2kmz(\'CentralValleyplus_Sierra_GPS_timeseries_NEW.kml\')"'
print('Converting kml to kmz using MATLAB script..this might not work..')
print(cmd)
os.system(cmd)