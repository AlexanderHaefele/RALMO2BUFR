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
        1085, 201151, 202130, 2121, 202000, 
        201000, 8021, 4025, 109000, 31002, 
        7007, 301021, 11003, 11004, 33002, 
        11006, 33002, 10071, 27079,) # 29 values

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
    codes_set(ibufr, 'uniqueIdentifierForProfile','PAYWP')
    codes_set(ibufr, 'observingPlatformManufacturerModel','PCL-1300')
    codes_set(ibufr, 'meanFrequency', 1.290000000000000000e+09)
    codes_set(ibufr, '#2#timeSignificance', 2)
    codes_set(ibufr, 'timePeriod', 20)
    codes_set(ibufr, '#1#height', 641)
    codes_set(ibufr, '#2#latitude', 4.681000000000000227e+01)
    codes_set(ibufr, '#2#longitude', 6.940000000000000391e+00)
    codes_set(ibufr, '#1#u', 6.200000000000000178e+00)
    codes_set(ibufr, '#1#v', 3.200000000000000178e+00)
    codes_set(ibufr, '#1#qualityInformation', 0)
    codes_set(ibufr, '#1#w', -5.999999999999999778e-02)
    codes_set(ibufr, '#2#qualityInformation', 0)
    codes_set(ibufr, '#1#verticalResolution', CODES_MISSING_LONG)
    codes_set(ibufr, '#1#horizontalWidthOfSampledVolume', CODES_MISSING_LONG)
    codes_set(ibufr, '#2#height', 784)
    codes_set(ibufr, '#3#latitude', 4.681000000000000227e+01)
    codes_set(ibufr, '#3#longitude', 6.940000000000000391e+00)
    codes_set(ibufr, '#2#u', 5.700000000000000178e+00)
    codes_set(ibufr, '#2#v', 3.200000000000000178e+00)
    codes_set(ibufr, '#3#qualityInformation', 0)
    codes_set(ibufr, '#2#w', -3.699999999999999956e-01)
    codes_set(ibufr, '#4#qualityInformation', 0)
    codes_set(ibufr, '#2#verticalResolution', CODES_MISSING_LONG)
    codes_set(ibufr, '#2#horizontalWidthOfSampledVolume', CODES_MISSING_LONG)
    codes_set(ibufr, '#3#height', 928)
    codes_set(ibufr, '#4#latitude', 4.681000000000000227e+01)
    codes_set(ibufr, '#4#longitude', 6.940000000000000391e+00)
    codes_set(ibufr, '#3#u', 5.900000000000000355e+00)
    codes_set(ibufr, '#3#v', 3.600000000000000089e+00)
    codes_set(ibufr, '#5#qualityInformation', 0)
    codes_set(ibufr, '#3#w', -1.100000000000000006e-01)
    codes_set(ibufr, '#6#qualityInformation', 0)
    codes_set(ibufr, '#3#verticalResolution', CODES_MISSING_LONG)
    codes_set(ibufr, '#3#horizontalWidthOfSampledVolume', CODES_MISSING_LONG)
    codes_set(ibufr, '#4#height', 1071)
    codes_set(ibufr, '#5#latitude', 4.681000000000000227e+01)
    codes_set(ibufr, '#5#longitude', 6.940000000000000391e+00)
    codes_set(ibufr, '#4#u', 7.000000000000000000e+00)
    codes_set(ibufr, '#4#v', 4.900000000000000355e+00)
    codes_set(ibufr, '#7#qualityInformation', 0)
    codes_set(ibufr, '#4#w', -7.000000000000000666e-02)
    codes_set(ibufr, '#8#qualityInformation', 0)
    codes_set(ibufr, '#4#verticalResolution', CODES_MISSING_LONG)
    codes_set(ibufr, '#4#horizontalWidthOfSampledVolume', CODES_MISSING_LONG)
    codes_set(ibufr, '#5#height', 1214)
    codes_set(ibufr, '#6#latitude', 4.681000000000000227e+01)
    codes_set(ibufr, '#6#longitude', 6.940000000000000391e+00)
    codes_set(ibufr, '#5#u', 7.900000000000000355e+00)
    codes_set(ibufr, '#5#v', 5.100000000000000533e+00)
    codes_set(ibufr, '#9#qualityInformation', 0)
    codes_set(ibufr, '#5#w', 1.000000000000000056e-01)
    codes_set(ibufr, '#10#qualityInformation', 0)
    codes_set(ibufr, '#5#verticalResolution', CODES_MISSING_LONG)
    codes_set(ibufr, '#5#horizontalWidthOfSampledVolume', CODES_MISSING_LONG)
    codes_set(ibufr, '#6#height', 1358)
    codes_set(ibufr, '#7#latitude', 4.681000000000000227e+01)
    codes_set(ibufr, '#7#longitude', 6.940000000000000391e+00)
    codes_set(ibufr, '#6#u', 7.800000000000000711e+00)
    codes_set(ibufr, '#6#v', 5.300000000000000711e+00)
    codes_set(ibufr, '#11#qualityInformation', 0)
    codes_set(ibufr, '#6#w', 0.000000000000000000e+00)
    codes_set(ibufr, '#12#qualityInformation', 0)
    codes_set(ibufr, '#6#verticalResolution', CODES_MISSING_LONG)
    codes_set(ibufr, '#6#horizontalWidthOfSampledVolume', CODES_MISSING_LONG)
    codes_set(ibufr, '#7#height', 1501)
    codes_set(ibufr, '#8#latitude', 4.681000000000000227e+01)
    codes_set(ibufr, '#8#longitude', 6.940000000000000391e+00)
    codes_set(ibufr, '#7#u', 8.099999999999999645e+00)
    codes_set(ibufr, '#7#v', 6.500000000000000000e+00)
    codes_set(ibufr, '#13#qualityInformation', 0)
    codes_set(ibufr, '#7#w', 8.000000000000000167e-02)
    codes_set(ibufr, '#14#qualityInformation', 0)
    codes_set(ibufr, '#7#verticalResolution', CODES_MISSING_LONG)
    codes_set(ibufr, '#7#horizontalWidthOfSampledVolume', CODES_MISSING_LONG)
    codes_set(ibufr, '#8#height', 1644)
    codes_set(ibufr, '#9#latitude', 4.681000000000000227e+01)
    codes_set(ibufr, '#9#longitude', 6.940000000000000391e+00)
    codes_set(ibufr, '#8#u', 8.599999999999999645e+00)
    codes_set(ibufr, '#8#v', 7.000000000000000000e+00)
    codes_set(ibufr, '#15#qualityInformation', 0)
    codes_set(ibufr, '#8#w', 1.100000000000000006e-01)
    codes_set(ibufr, '#16#qualityInformation', 0)
    codes_set(ibufr, '#8#verticalResolution', CODES_MISSING_LONG)
    codes_set(ibufr, '#8#horizontalWidthOfSampledVolume', CODES_MISSING_LONG)
    codes_set(ibufr, '#9#height', 1788)
    codes_set(ibufr, '#10#latitude', 4.681000000000000227e+01)
    codes_set(ibufr, '#10#longitude', 6.940000000000000391e+00)
    codes_set(ibufr, '#9#u', 8.800000000000000711e+00)
    codes_set(ibufr, '#9#v', 7.900000000000000355e+00)
    codes_set(ibufr, '#17#qualityInformation', 0)
    codes_set(ibufr, '#9#w', -5.999999999999999778e-02)
    codes_set(ibufr, '#18#qualityInformation', 0)
    codes_set(ibufr, '#9#verticalResolution', CODES_MISSING_LONG)
    codes_set(ibufr, '#9#horizontalWidthOfSampledVolume', CODES_MISSING_LONG)
    codes_set(ibufr, '#10#height', 1931)
    codes_set(ibufr, '#11#latitude', 4.681000000000000227e+01)
    codes_set(ibufr, '#11#longitude', 6.940000000000000391e+00)
    codes_set(ibufr, '#10#u', 8.800000000000000711e+00)
    codes_set(ibufr, '#10#v', 8.800000000000000711e+00)
    codes_set(ibufr, '#19#qualityInformation', 0)
    codes_set(ibufr, '#10#w', 5.999999999999999778e-02)
    codes_set(ibufr, '#20#qualityInformation', 0)
    codes_set(ibufr, '#10#verticalResolution', CODES_MISSING_LONG)
    codes_set(ibufr, '#10#horizontalWidthOfSampledVolume', CODES_MISSING_LONG)
    codes_set(ibufr, '#11#height', 2074)
    codes_set(ibufr, '#12#latitude', 4.681000000000000227e+01)
    codes_set(ibufr, '#12#longitude', 6.940000000000000391e+00)
    codes_set(ibufr, '#11#u', 8.900000000000000355e+00)
    codes_set(ibufr, '#11#v', 8.900000000000000355e+00)
    codes_set(ibufr, '#21#qualityInformation', 0)
    codes_set(ibufr, '#11#w', 1.700000000000000122e-01)
    codes_set(ibufr, '#22#qualityInformation', 0)
    codes_set(ibufr, '#11#verticalResolution', CODES_MISSING_LONG)
    codes_set(ibufr, '#11#horizontalWidthOfSampledVolume', CODES_MISSING_LONG)
    codes_set(ibufr, '#12#height', 2218)
    codes_set(ibufr, '#13#latitude', 4.681000000000000227e+01)
    codes_set(ibufr, '#13#longitude', 6.940000000000000391e+00)
    codes_set(ibufr, '#12#u', 8.400000000000000355e+00)
    codes_set(ibufr, '#12#v', 9.300000000000000711e+00)
    codes_set(ibufr, '#23#qualityInformation', 0)
    codes_set(ibufr, '#12#w', 7.000000000000000666e-02)
    codes_set(ibufr, '#24#qualityInformation', 0)
    codes_set(ibufr, '#12#verticalResolution', CODES_MISSING_LONG)
    codes_set(ibufr, '#12#horizontalWidthOfSampledVolume', CODES_MISSING_LONG)
    codes_set(ibufr, '#13#height', 2361)
    codes_set(ibufr, '#14#latitude', 4.681000000000000227e+01)
    codes_set(ibufr, '#14#longitude', 6.940000000000000391e+00)
    codes_set(ibufr, '#13#u', 8.800000000000000711e+00)
    codes_set(ibufr, '#13#v', 6.900000000000000355e+00)
    codes_set(ibufr, '#25#qualityInformation', 0)
    codes_set(ibufr, '#13#w', 1.600000000000000033e-01)
    codes_set(ibufr, '#26#qualityInformation', 0)
    codes_set(ibufr, '#13#verticalResolution', CODES_MISSING_LONG)
    codes_set(ibufr, '#13#horizontalWidthOfSampledVolume', CODES_MISSING_LONG)
    codes_set(ibufr, '#14#height', 2504)
    codes_set(ibufr, '#15#latitude', 4.681000000000000227e+01)
    codes_set(ibufr, '#15#longitude', 6.940000000000000391e+00)
    codes_set(ibufr, '#14#u', 9.300000000000000711e+00)
    codes_set(ibufr, '#14#v', 5.400000000000000355e+00)
    codes_set(ibufr, '#27#qualityInformation', 0)
    codes_set(ibufr, '#14#w', 2.700000000000000178e-01)
    codes_set(ibufr, '#28#qualityInformation', 0)
    codes_set(ibufr, '#14#verticalResolution', CODES_MISSING_LONG)
    codes_set(ibufr, '#14#horizontalWidthOfSampledVolume', CODES_MISSING_LONG)
    codes_set(ibufr, '#15#height', 2648)
    codes_set(ibufr, '#16#latitude', 4.681000000000000227e+01)
    codes_set(ibufr, '#16#longitude', 6.940000000000000391e+00)
    codes_set(ibufr, '#15#u', 1.070000000000000107e+01)
    codes_set(ibufr, '#15#v', 3.900000000000000355e+00)
    codes_set(ibufr, '#29#qualityInformation', 0)
    codes_set(ibufr, '#15#w', 2.000000000000000111e-01)
    codes_set(ibufr, '#30#qualityInformation', 0)
    codes_set(ibufr, '#15#verticalResolution', CODES_MISSING_LONG)
    codes_set(ibufr, '#15#horizontalWidthOfSampledVolume', CODES_MISSING_LONG)
    codes_set(ibufr, '#16#height', 2791)
    codes_set(ibufr, '#17#latitude', 4.681000000000000227e+01)
    codes_set(ibufr, '#17#longitude', 6.940000000000000391e+00)
    codes_set(ibufr, '#16#u', 1.160000000000000142e+01)
    codes_set(ibufr, '#16#v', 3.100000000000000089e+00)
    codes_set(ibufr, '#31#qualityInformation', 0)
    codes_set(ibufr, '#16#w', 2.099999999999999922e-01)
    codes_set(ibufr, '#32#qualityInformation', 0)
    codes_set(ibufr, '#16#verticalResolution', CODES_MISSING_LONG)
    codes_set(ibufr, '#16#horizontalWidthOfSampledVolume', CODES_MISSING_LONG)
    codes_set(ibufr, '#17#height', 2934)
    codes_set(ibufr, '#18#latitude', 4.681000000000000227e+01)
    codes_set(ibufr, '#18#longitude', 6.940000000000000391e+00)
    codes_set(ibufr, '#17#u', 1.220000000000000107e+01)
    codes_set(ibufr, '#17#v', 2.600000000000000089e+00)
    codes_set(ibufr, '#33#qualityInformation', 0)
    codes_set(ibufr, '#17#w', 1.600000000000000033e-01)
    codes_set(ibufr, '#34#qualityInformation', 0)
    codes_set(ibufr, '#17#verticalResolution', CODES_MISSING_LONG)
    codes_set(ibufr, '#17#horizontalWidthOfSampledVolume', CODES_MISSING_LONG)
    codes_set(ibufr, '#18#height', 3078)
    codes_set(ibufr, '#19#latitude', 4.681000000000000227e+01)
    codes_set(ibufr, '#19#longitude', 6.940000000000000391e+00)
    codes_set(ibufr, '#18#u', 1.380000000000000071e+01)
    codes_set(ibufr, '#18#v', -7.000000000000000666e-01)
    codes_set(ibufr, '#35#qualityInformation', 0)
    codes_set(ibufr, '#18#w', 1.100000000000000006e-01)
    codes_set(ibufr, '#36#qualityInformation', 0)
    codes_set(ibufr, '#18#verticalResolution', CODES_MISSING_LONG)
    codes_set(ibufr, '#18#horizontalWidthOfSampledVolume', CODES_MISSING_LONG)
    codes_set(ibufr, '#19#height', 3221)
    codes_set(ibufr, '#20#latitude', 4.681000000000000227e+01)
    codes_set(ibufr, '#20#longitude', 6.940000000000000391e+00)
    codes_set(ibufr, '#19#u', 1.440000000000000036e+01)
    codes_set(ibufr, '#19#v', -2.300000000000000266e+00)
    codes_set(ibufr, '#37#qualityInformation', 0)
    codes_set(ibufr, '#19#w', 4.000000000000000083e-02)
    codes_set(ibufr, '#38#qualityInformation', 0)
    codes_set(ibufr, '#19#verticalResolution', CODES_MISSING_LONG)
    codes_set(ibufr, '#19#horizontalWidthOfSampledVolume', CODES_MISSING_LONG)
    codes_set(ibufr, '#20#height', 3364)
    codes_set(ibufr, '#21#latitude', 4.681000000000000227e+01)
    codes_set(ibufr, '#21#longitude', 6.940000000000000391e+00)
    codes_set(ibufr, '#20#u', 1.500000000000000000e+01)
    codes_set(ibufr, '#20#v', -2.400000000000000355e+00)
    codes_set(ibufr, '#39#qualityInformation', 0)
    codes_set(ibufr, '#20#w', 8.999999999999999667e-02)
    codes_set(ibufr, '#40#qualityInformation', 0)
    codes_set(ibufr, '#20#verticalResolution', CODES_MISSING_LONG)
    codes_set(ibufr, '#20#horizontalWidthOfSampledVolume', CODES_MISSING_LONG)
    codes_set(ibufr, '#21#height', 3508)
    codes_set(ibufr, '#22#latitude', 4.681000000000000227e+01)
    codes_set(ibufr, '#22#longitude', 6.940000000000000391e+00)
    codes_set(ibufr, '#21#u', 1.669999999999999929e+01)
    codes_set(ibufr, '#21#v', -4.500000000000000000e+00)
    codes_set(ibufr, '#41#qualityInformation', 0)
    codes_set(ibufr, '#21#w', 5.000000000000000278e-02)
    codes_set(ibufr, '#42#qualityInformation', 0)
    codes_set(ibufr, '#21#verticalResolution', CODES_MISSING_LONG)
    codes_set(ibufr, '#21#horizontalWidthOfSampledVolume', CODES_MISSING_LONG)
    codes_set(ibufr, '#22#height', 3651)
    codes_set(ibufr, '#23#latitude', 4.681000000000000227e+01)
    codes_set(ibufr, '#23#longitude', 6.940000000000000391e+00)
    codes_set(ibufr, '#22#u', 1.910000000000000142e+01)
    codes_set(ibufr, '#22#v', -5.800000000000000711e+00)
    codes_set(ibufr, '#43#qualityInformation', 0)
    codes_set(ibufr, '#22#w', 7.000000000000000666e-02)
    codes_set(ibufr, '#44#qualityInformation', 0)
    codes_set(ibufr, '#22#verticalResolution', CODES_MISSING_LONG)
    codes_set(ibufr, '#22#horizontalWidthOfSampledVolume', CODES_MISSING_LONG)

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
