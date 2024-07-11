#  This program was automatically generated with bufr_dump -Epython
#  Using ecCodes version: 2.25.0

from __future__ import print_function
import traceback
import sys
from eccodes import *
import pandas


def bufr_encode(data):
    
    # set the number of levels to encode
    levels = 1
    
    # BUFR structure
    ibufr = codes_bufr_new_from_samples('BUFR4')
    ivalues = (levels ,)
    codes_set_array(ibufr, 'inputExtendedDelayedDescriptorReplicationFactor', ivalues)
    codes_set(ibufr, 'edition', 4)
    codes_set(ibufr, 'masterTableNumber', 0)
    codes_set(ibufr, 'bufrHeaderCentre', 74)
    codes_set(ibufr, 'bufrHeaderSubCentre', 0)
    codes_set(ibufr, 'updateSequenceNumber', 0)
    codes_set(ibufr, 'dataCategory', 2)
    codes_set(ibufr, 'internationalDataSubCategory', 10)
    codes_set(ibufr, 'dataSubCategory', 0)
    codes_set(ibufr, 'masterTablesVersionNumber', 35)
    codes_set(ibufr, 'localTablesVersionNumber', 0)
    codes_set(ibufr, 'typicalYear', 2024)
    codes_set(ibufr, 'typicalMonth', 7)
    codes_set(ibufr, 'typicalDay', 4)
    codes_set(ibufr, 'typicalHour', 12)
    codes_set(ibufr, 'typicalMinute', 30)
    codes_set(ibufr, 'typicalSecond', 0)
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
    codes_set(ibufr, 'year', 2024)
    codes_set(ibufr, 'month', 7)
    codes_set(ibufr, 'day', 4)
    codes_set(ibufr, 'hour', 12)
    codes_set(ibufr, 'minute', 30)
    codes_set(ibufr, 'upperAirRemoteSensingInstrumentType', 6)
    codes_set(ibufr, 'uniqueIdentifierForProfile','PAYRL')
    codes_set(ibufr, 'observingPlatformManufacturerModel','RALMO')
    codes_set(ibufr, '#2#timeSignificance', 2)
    codes_set(ibufr, 'timePeriod', 1800)
    # data profile section
    for i in range(levels):
        print(i)
        codes_set(ibufr, '#1#height', data.level[i])
        codes_set(ibufr, '#2#latitude', 4.681000000000000227e+01)
        codes_set(ibufr, '#2#longitude', 6.940000000000000391e+00)
        codes_set(ibufr, '#1#qualityOfFollowingValue', 0)
        codes_set(ibufr, '#1#mixingRatio', data.hum[i]/1000)
        codes_set(ibufr, '#1#measurementUncertaintyExpression', 0)
        codes_set(ibufr, '#1#measurementUncertaintySignificance', 0)
        codes_set(ibufr, '#2#mixingRatio', data.hum_U[i]/1000)
        codes_set(ibufr, '#2#measurementUncertaintyExpression', 31)
        codes_set(ibufr, '#2#measurementUncertaintySignificance', 31)
        codes_set(ibufr, '#1#airTemperature', data.temp[i])
        codes_set(ibufr, '#3#measurementUncertaintyExpression', 0)
        codes_set(ibufr, '#3#measurementUncertaintySignificance', 0)
        codes_set(ibufr, '#2#airTemperature', data.temp_U[i])
        codes_set(ibufr, '#4#measurementUncertaintyExpression', 31)
        codes_set(ibufr, '#4#measurementUncertaintySignificance', 31)
        codes_set(ibufr, '#1#verticalResolution', data.vert_res[i])
    
    # Encode the keys back in the data section
    codes_set(ibufr, 'pack', 1)

    outfile = open('outfile.bufr', 'wb')
    codes_write(ibufr, outfile)
    print ("Created output BUFR file 'outfile.bufr'")
    codes_release(ibufr)


def main():
    
    # read csv file
    csvfile = 'ralmo20240709000000.txt'
    # read data
    data = pandas.read_csv(csvfile,skiprows=3,sep='|',na_values=[10000000],names=["id","termin","track_type","prof_type","type","level","hum","hum_U","vert_res","temp","temp_U","dum4909","dum 4910","dum4911","dum4912","dum4913","dum4914","dum4915"])
    
    try:
        bufr_encode(data)
    except CodesInternalError as err:
        traceback.print_exc(file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
