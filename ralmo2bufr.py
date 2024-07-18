#  This program was automatically generated with bufr_dump -Epython
#  Using ecCodes version: 2.25.0

from __future__ import print_function
import traceback
import sys
from eccodes import *
import pandas


def bufr_encode(data,outfile):
    
    # set the number of levels to encode
    levels = data.hum.size

    # create time information
    dt = pandas.to_datetime(data.mytime[data.index[0]])
    
    # BUFR structure
    ibufr = codes_bufr_new_from_samples('BUFR4')
    ivalues = (levels ,)
    codes_set_array(ibufr, 'inputExtendedDelayedDescriptorReplicationFactor', ivalues)
    codes_set(ibufr, 'edition', 4)
    codes_set(ibufr, 'masterTableNumber', 0)
    codes_set(ibufr, 'bufrHeaderCentre', 215)
    codes_set(ibufr, 'bufrHeaderSubCentre', 0)
    codes_set(ibufr, 'updateSequenceNumber', 0)
    codes_set(ibufr, 'dataCategory', 2)
    codes_set(ibufr, 'internationalDataSubCategory', 10)
    codes_set(ibufr, 'dataSubCategory', 0)
    codes_set(ibufr, 'masterTablesVersionNumber', 35)
    codes_set(ibufr, 'localTablesVersionNumber', 0)
    codes_set(ibufr, 'typicalYear', dt.year)
    codes_set(ibufr, 'typicalMonth', dt.month)
    codes_set(ibufr, 'typicalDay', dt.day)
    codes_set(ibufr, 'typicalHour', dt.hour)
    codes_set(ibufr, 'typicalMinute', dt.minute)
    codes_set(ibufr, 'typicalSecond', dt.second)
    codes_set(ibufr, 'numberOfSubsets', 1)
    codes_set(ibufr, 'observedData', 1)
    codes_set(ibufr, 'compressedData', 0)
    ivalues = (
        301150, 301001, 5001, 6001, 7030, 
        8021, 301011, 301012, 2006, 1079, 
        1085, 8021, 4026, 116000, 31002, 
        7007, 301021, 33021, 13002, 8092, 
        8093, 13002, 8092, 8093, 12001, 
        8092, 8093, 12001, 8092, 8093, 
        10071,) # 31 values

    # Create the structure of the data section
    codes_set_array(ibufr, 'unexpandedDescriptors', ivalues)
    # data header section
    codes_set(ibufr, 'wigosIdentifierSeries', 0)
    codes_set(ibufr, 'wigosIssuerOfIdentifier', 20000)
    codes_set(ibufr, 'wigosIssueNumber', 0)
    codes_set(ibufr, 'wigosLocalIdentifierCharacter','06610')
    codes_set(ibufr, 'blockNumber', 6)
    codes_set(ibufr, 'stationNumber', 610)
    codes_set(ibufr, '#1#latitude', 4.681000000000000227e+01)
    codes_set(ibufr, '#1#longitude', 6.940000000000000391e+00)
    codes_set(ibufr, 'heightOfStationGroundAboveMeanSeaLevel', 4.910000000000000000e+02)
    codes_set(ibufr, '#1#timeSignificance', 29)
    codes_set(ibufr, 'year', dt.year)
    codes_set(ibufr, 'month', dt.month)
    codes_set(ibufr, 'day', dt.day)
    codes_set(ibufr, 'hour', dt.hour)
    codes_set(ibufr, 'minute', dt.minute)
    codes_set(ibufr, 'upperAirRemoteSensingInstrumentType', 6)
    codes_set(ibufr, 'uniqueIdentifierForProfile','PAYRL')
    codes_set(ibufr, 'observingPlatformManufacturerModel','RALMO')
    codes_set(ibufr, '#2#timeSignificance', 2)
    codes_set(ibufr, 'timePeriod', 1800)
    # data profile section
    for i in range(levels):
        codes_set(ibufr, '#'+str(i+1)+'#height', data.level[data.index[i]])
        codes_set(ibufr, '#'+str(i+2)+'#latitude', 4.681000000000000227e+01)
        codes_set(ibufr, '#'+str(i+2)+'#longitude', 6.940000000000000391e+00)
        codes_set(ibufr, '#'+str(i+1)+'#qualityOfFollowingValue', 0)
        codes_set(ibufr, '#'+str(2*i+1)+'#mixingRatio', data.hum[data.index[i]]/1000)
        codes_set(ibufr, '#'+str(4*i+1)+'#measurementUncertaintyExpression', 0)
        codes_set(ibufr, '#'+str(4*i+1)+'#measurementUncertaintySignificance', 0)
        codes_set(ibufr, '#'+str(2*i+2)+'#mixingRatio', data.hum_U[data.index[i]]/1000)
        codes_set(ibufr, '#'+str(4*i+2)+'#measurementUncertaintyExpression', 31)
        codes_set(ibufr, '#'+str(4*i+2)+'#measurementUncertaintySignificance', 31)
        codes_set(ibufr, '#'+str(2*i+1)+'#airTemperature', data.temp[data.index[i]])
        codes_set(ibufr, '#'+str(4*i+3)+'#measurementUncertaintyExpression', 0)
        codes_set(ibufr, '#'+str(4*i+3)+'#measurementUncertaintySignificance', 0)
        codes_set(ibufr, '#'+str(2*i+2)+'#airTemperature', data.temp_U[data.index[i]])
        codes_set(ibufr, '#'+str(4*i+4)+'#measurementUncertaintyExpression', 31)
        codes_set(ibufr, '#'+str(4*i+4)+'#measurementUncertaintySignificance', 31)
        codes_set(ibufr, '#'+str(i+1)+'#verticalResolution', data.vert_res[data.index[i]])
    
    # Encode the keys back in the data section
    codes_set(ibufr, 'pack', 1)

    outfile = open(outfile, 'wb')
    codes_write(ibufr, outfile)
    print ("Created output BUFR file 'outfile.bufr'")
    codes_release(ibufr)


def main():
    
    # read csv file
    csvfile = 'ralmo20240709.txt'
    # read data
    data_day = pandas.read_csv(csvfile,skiprows=3,sep='|',parse_dates={'mytime':[1]},na_values=[10000000],names=["id","termin","track_type","prof_type","type","level","hum","hum_U","vert_res","temp","temp_U","dum4909","dum 4910","dum4911","dum4912","dum4913","dum4914","dum4915"])
    # create time array
    tt = pandas.date_range("2024-07-09 00:00:00","2024-07-09 23:59:00",freq="30min")
    
    # loop over time array
    for i in tt:
        data = data_day[data_day.mytime==i]
        # continue with loop if data is empty
        if data.hum.size==0:
            continue

        # remove nan's in hum
        data = data[data.hum.notna() & data.temp.notna()]

        try:
            bufr_encode(data,'ralmo'+i.strftime('%Y%m%d%H%M')+'.bufr')
        except CodesInternalError as err:
            traceback.print_exc(file=sys.stderr)
            return 1


if __name__ == "__main__":
    sys.exit(main())
