import pywapi;

def yaholo():
    ryaholo = pywapi.get_weather_from_yahoo('77001', 'metric')
    return ryaholo
def noaalo():
    rnoaalo = pywapi.get_weather_from_noaa('KHOU')
    return rnoaalo

def weatlo():
    rweatlo = pywapi.get_weather_from_weather_com('77001')
    return rweatlo
