import pywapi;

def yahony():
    ryahony = pywapi.get_weather_from_yahoo('10010', 'metric')
    return ryahony
def noaany():
    rnoaany = pywapi.get_weather_from_noaa('KNYC')
    return rnoaany

def weatny():
    rweatny = pywapi.get_weather_from_weather_com('10010')
    return rweatny
