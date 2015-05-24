import pywapi;

def yahola():
    ryahola = pywapi.get_weather_from_yahoo('90007', 'metric')
    return ryahola
def noaala():
    rnoaala = pywapi.get_weather_from_noaa('KCQT')
    return rnoaala

def weatla():
    rweatla = pywapi.get_weather_from_weather_com('90007')
    return rweatla
