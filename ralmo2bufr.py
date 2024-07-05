#  This program was automatically generated with bufr_dump -Epython
#  Using ecCodes version: 2.25.0

from __future__ import print_function
import traceback
import sys
from eccodes import *


def bufr_encode():
    ibufr = codes_bufr_new_from_samples('BUFR4')
    ivalues = (22 ,)
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
    codes_set(ibufr, '#1#height', 641)
    codes_set(ibufr, '#2#latitude', 4.681000000000000227e+01)
    codes_set(ibufr, '#2#longitude', 6.940000000000000391e+00)
    codes_set(ibufr, '#1#qualityOfFollowingValue', 0)
    codes_set(ibufr, '#1#mixingRatio', 0.01)
    codes_set(ibufr, '#1#measurementUncertaintyExpression', 0)
    codes_set(ibufr, '#1#measurementUncertaintySignificance', 0)
    codes_set(ibufr, '#1#mixingRatio', 0.002)
    codes_set(ibufr, '#1#measurementUncertaintyExpression', 31)
    codes_set(ibufr, '#1#measurementUncertaintySignificance', 31)
    codes_set(ibufr, '#1#airTemperature', 300)
    codes_set(ibufr, '#1#measurementUncertaintyExpression', 0)
    codes_set(ibufr, '#1#measurementUncertaintySignificance', 0)
    codes_set(ibufr, '#1#airTemperature', 1)
    codes_set(ibufr, '#1#measurementUncertaintyExpression', 31)
    codes_set(ibufr, '#1#measurementUncertaintySignificance', 31)
    codes_set(ibufr, '#1#verticalResolution', 30)
    
    # Encode the keys back in the data section
    codes_set(ibufr, 'pack', 1)

    outfile = open('outfile.bufr', 'wb')
    codes_write(ibufr, outfile)
    print ("Created output BUFR file 'outfile.bufr'")
    codes_release(ibufr)


def main():
    try:
        bufr_encode()
    except CodesInternalError as err:
        traceback.print_exc(file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
