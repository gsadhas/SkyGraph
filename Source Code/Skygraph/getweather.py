import pywapi
import HTMLParser
import pprint
#pp = pprint.PrettyPrinter(indent=4)
#class fetch():
def getweather():
    data = pywapi.get_weather_from_noaa('KMDW')
    return data

def getww():
    data2 = pywapi.get_weather_from_weather_com('60607')
    return data2

"""loca = data['location']
    obst = data['observation_time']
    wea = data['weather']
    tempf = data['temp_f']
    tempc =  data['temp_c']
    dewpointf = data['dewpoint_f']
    dewpointc = data['dewpoint_c']
    hum = data['relative_humidity']
    wind = data['wind_string']
    chillf = data['windchill_f']
    chillc = data['windchill_c']

    return{'loca':loca, 'obst':obst,'wea':wea,'tempf':tempf,'tempc':tempc,'dewpointf':dewpointf,'dewpointc':dewpointc,'hum':hum,
           'wind':wind,'chillf':chillf,'chillc':chillc}"""

def yahoow():
    result2 = pywapi.get_weather_from_yahoo('60607', 'metric')
    return result2


        #html_parser = HTMLParser.HTMLParser()
    #unesc = html_parser.unescape(result2['html_description'])
    #return unesc
  #  areas = ['KFEP','KALN','KARR']
 #   for loc in areas:
#        location = pywapi.get_weather_from_noaa(loc)


"""for loc in areas:
    data = pywapi.get_weather_from_noaa(loc)
    #print data
    print ''
    print 'Location  :'+data['location']
    print 'Last Updated : ' + data['observation_time']
    print 'Weather : ' + data['weather']
    print 'Temperature : '+ data['temp_f'] +'F ('+ data['temp_c']+' C)'
    print 'Dewpoint :' + data['dewpoint_f']+'F ('+data['dewpoint_c']+' C)'
    print 'Relative Humidity :' + data['relative_humidity']+'%'
    print 'Wind :' + data['wind_string']
    print 'Wind Chill :'+data['windchill_f']+'F '+data['windchill_c']+'C'"""


