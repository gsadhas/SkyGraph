import pywapi;

def yahoho():
    ryahoho = pywapi.get_weather_from_yahoo('77001', 'metric')
    return ryahoho
def noaaho():
    rnoaaho = pywapi.get_weather_from_noaa('KHOU')
    return rnoaaho

def weatho():
    rweatho = pywapi.get_weather_from_weather_com('77001')
    return rweatho
