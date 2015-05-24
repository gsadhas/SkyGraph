import pywapi;

def yahosa():
    ryahosa = pywapi.get_weather_from_yahoo('94102', 'metric')
    return ryahosa
def noaasa():
    rnoaasa = pywapi.get_weather_from_noaa('KMRY')
    return rnoaasa

def weatsa():
    rweatsa = pywapi.get_weather_from_weather_com('94102')
    return rweatsa
