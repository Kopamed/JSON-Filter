import pandas as pd
import demjson as dj
import json
from beeprint import pp


def f_dict(d):
    r = {}
    currentHotel = {}
    currentConnection = {}
    
    for i in range(len(d["tour"]["items"])-1):
        r[d["tour"]["items"][str(i)]["currentHub"]["hub"]["id"]] = {"days":d["tour"]["items"][str(i)]["currentHub"]["hub"]["days"]["number"], "nights": d["tour"]["items"][str(i)]["currentHub"]["hub"]["nights"]["number"], "startDate": d["tour"]["items"][str(i)]["currentHub"]["hub"]["date"]["startDate"], "endDate": d["tour"]["items"][str(i)]["currentHub"]["hub"]["date"]["endDate"]}
        currentHotel[d["tour"]["items"][str(i)]["currentHub"]["hub"]["id"]] = {"totalPrice": d["tour"]["items"][str(i)]["currentHub"]["totalPrice"], "totalHotel": d["tour"]["items"][str(i)]["currentHub"]["totalHotel"], "totalPriceOnePercon": d["tour"]["items"][str(i)]["currentHub"]["totalPriceOnePercon"], "totalPricePerDay": d["tour"]["items"][str(i)]["currentHub"]["totalPricePerDay"], "totalPriceActivity": d["tour"]["items"][str(i)]["currentHub"]["totalPriceActivity"]}
        currentConnection[d["tour"]["items"][str(i)]["currentHub"]["hub"]["id"]] = {"id": d["tour"]["items"]["1"]["currentConnection"]["id"], "entity_id": d["tour"]["items"]["1"]["currentConnection"]["entity_id"], "name": d["tour"]["items"]["1"]["currentConnection"]["name"], "type": d["tour"]["items"]["1"]["currentConnection"]["type"], "duration": d["tour"]["items"]["1"]["currentConnection"]["duration"], "nights": d["tour"]["items"]["1"]["currentConnection"]["nights"], "fromHub": d["tour"]["items"]["1"]["currentConnection"]["fromHub"], "toCity": d["tour"]["items"]["1"]["currentConnection"]["toCity"], "toHub": d["tour"]["items"]["1"]["currentConnection"]["toHub"]}
    pp(r)
    pp(currentConnection)
    pp(currentHotel)




f = open("c.json", "r")
f = json.loads(f.read())
f_dict(f)