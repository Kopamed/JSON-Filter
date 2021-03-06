import json
import demjson as dj
import pandas as pd







def f_dict(d):
    r = {}
    currentHotel = {}
    currentConnection = {}
    
    for i in range(len(d["tour"]["items"])-1):
        r[d["tour"]["items"][str(i)]["currentHub"]["hub"]["id"]] = {"days":d["tour"]["items"][str(i)]["currentHub"]["hub"]["days"]["number"], "nights": d["tour"]["items"][str(i)]["currentHub"]["hub"]["nights"]["number"], "startDate": d["tour"]["items"][str(i)]["currentHub"]["hub"]["date"]["startDate"], "endDate": d["tour"]["items"][str(i)]["currentHub"]["hub"]["date"]["endDate"]}
        currentHotel[d["tour"]["items"][str(i)]["currentHub"]["hub"]["id"]] = {"totalPrice": d["tour"]["items"][str(i)]["currentHub"]["totalPrice"], "totalHotel": d["tour"]["items"][str(i)]["currentHub"]["totalHotel"], "totalPriceOnePercon": d["tour"]["items"][str(i)]["currentHub"]["totalPriceOnePercon"], "totalPricePerDay": d["tour"]["items"][str(i)]["currentHub"]["totalPricePerDay"], "totalPriceActivity": d["tour"]["items"][str(i)]["currentHub"]["totalPriceActivity"]}
        currentConnection[d["tour"]["items"][str(i)]["currentHub"]["hub"]["id"]] = {"id": d["tour"]["items"]["1"]["currentConnection"]["id"], "entity_id": d["tour"]["items"]["1"]["currentConnection"]["entity_id"], "name": d["tour"]["items"]["1"]["currentConnection"]["name"], "type": d["tour"]["items"]["1"]["currentConnection"]["type"], "duration": d["tour"]["items"]["1"]["currentConnection"]["duration"], "nights": d["tour"]["items"]["1"]["currentConnection"]["nights"], "fromHub": d["tour"]["items"]["1"]["currentConnection"]["fromHub"], "toCity": d["tour"]["items"]["1"]["currentConnection"]["toCity"], "toHub": d["tour"]["items"]["1"]["currentConnection"]["toHub"]}

return (r, currentConnection, currentHotel)













'''
def extract_tour(txt):
    
    if txt[0] != "{":
        txt = "{" + txt + "}"
    
    obj = json.loads(txt)
    final = {}
    
    final["tour"] = {"templateOptions": {"price": obj["tour"]["templateOptions"]["price"]},"ttPrice": obj["tour"]["ttPrice"],"totalDays": obj["tour"]["totalDays"], "travelers": obj["tour"]["travelers"], "date": obj["tour"]["date"], "items": {"0": {"currentHub": {"hub": {"id": obj["tour"]["items"]["0"]["currentHub"]["hub"]["id"], "name": obj["tour"]["items"]["0"]["currentHub"]["hub"]["name"], "country": obj["tour"]["items"]["0"]["currentHub"]["hub"]["country"], "countryCode": obj["tour"]["items"]["0"]["currentHub"]["hub"]["countryCode"], "days": {"number": obj["tour"]["items"]["0"]["currentHub"]["hub"]["days"]["number"], "formatted": obj["tour"]["items"]["0"]["currentHub"]["hub"]["days"]["formatted"]}, "nights": {"number": obj["tour"]["items"]["0"]["currentHub"]["hub"]["nights"]["number"], "formatted": obj["tour"]["items"]["0"]["currentHub"]["hub"]["nights"]["formatted"]}, "geolocation": {"0": obj["tour"]["items"]["0"]["currentHub"]["hub"]["geolocation"]["0"] ,"1": obj["tour"]["items"]["0"]["currentHub"]["hub"]["geolocation"]["1"]}, "date": {"startDate": obj["tour"]["items"]["0"]["currentHub"]["hub"]["date"]["startDate"], "endDate": obj["tour"]["items"]["0"]["currentHub"]["hub"]["date"]["endDate"]}}}, "totalHotel": obj["tour"]["items"]["0"]["currentHub"]["totalHotel"], "totalPrice": obj["tour"]["items"]["0"]["currentHub"]["totalPrice"], "totalPriceOnePercon": obj["tour"]["items"]["0"]["currentHub"]["totalPriceOnePercon"], "totalPriceOnePerconFormatted": obj["tour"]["items"]["0"]["currentHub"]["totalPriceOnePerconFormatted"], "totalPricePerDay": obj["tour"]["items"]["0"]["currentHub"]["totalPricePerDay"], "totalPriceActivity": obj["tour"]["items"]["0"]["currentHub"]["totalPriceActivity"]}, "1" : {"currentConnections" : {"id": obj["tour"]["items"]["1"]["currentConnection"]["id"], "entity_id": obj["tour"]["items"]["1"]["currentConnection"]["entity_id"], "name": obj["tour"]["items"]["1"]["currentConnection"]["name"], "type": obj["tour"]["items"]["1"]["currentConnection"]["type"], "duration": obj["tour"]["items"]["1"]["currentConnection"]["duration"], "nights": obj["tour"]["items"]["1"]["currentConnection"]["nights"], "rating": obj["tour"]["items"]["1"]["currentConnection"]["rating"], "fromCity" : obj["tour"]["items"]["1"]["currentConnection"]["fromCity"], "fromHub": obj["tour"]["items"]["1"]["currentConnection"]["fromHub"], "toCity": obj["tour"]["items"]["1"]["currentConnection"]["toCity"], "toHub": obj["tour"]["items"]["1"]["currentConnection"]["toHub"], "geolocation": {"0": obj["tour"]["items"]["1"]["currentConnection"]["geolocation"]["0"], "1": obj["tour"]["items"]["1"]["currentConnection"]["geolocation"]["1"]}, "departureCountryCode": obj["tour"]["items"]["1"]["currentConnection"]["departureCountryCode"], "arrivalCountryCode": obj["tour"]["items"]["1"]["currentConnection"]["arrivalCountryCode"]}}}}
    
    
    return final 
    
        

def extract_wishlist(txt):
    
    if txt[0] != "{":
        txt = "{" + txt + "}"

    obj = json.loads(txt)
    final = {}
    final["tour"] = {"items":{"0":{"currentHu":{"hu":{"id": obj["tour"]["items"]["0"]["currentHu"]["hu"]["id"], "name": obj["tour"]["items"]["0"]["currentHu"]["hu"]["name"], "country": obj["tour"]["items"]["0"]["currentHu"]["hu"]["country"], "countryCode": obj["tour"]["items"]["0"]["currentHu"]["hu"]["countryCode"], "geolocation": obj["tour"]["items"]["0"]["currentHu"]["hu"]["geolocation"]}, "activities": obj["tour"]["items"]["0"]["currentHu"]["activities"]}}}}
    
    
    return final
'''

