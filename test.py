import pandas as pd
import json
from beeprint import pp
import demjson as dj


    
df = pd.read_csv (r'TripTile_objects.csv')
a = "{" + df[df.columns[2]].iloc[0] + "}"
pp(dj.decode(a))
#hubs



'''

import pandas as pd
import demjson as dj
import json


df = pd.read_csv (r'TripTile_objects.csv')
j = json.loads(df.to_json())

#print (pp(j))

for i in range(len(j["1"])):
    #the json will come from here
    current_json = dj.decode(j["1"][str(i)])
    pp(current_json["tour"])

f = open("c.json", "r")
f = json.loads(f.read())

#pp(f["tour"]["items"])
print(len(f["tour"]["items"]))
for i in range(len(f["tour"]["items"])):
    print(f["tour"]["items"][str(i)]["currentHub"]["hub"]["id"])
    print(f["tour"]["items"][str(i)]["currentHub"]["hub"]["name"])
    

def f_dict(d):
    r = {}
    
    
    for i in range(len(d["tour"]["items"])-1):
        r[d["tour"]["items"][str(i)]["currentHub"]["hub"]["id"]] = {"days":d["tour"]["items"][str(i)]["currentHub"]["hub"]["days"]["number"], "nights": d["tour"]["items"][str(i)]["currentHub"]["hub"]["nights"]["number"], "startDate": d["tour"]["items"][str(i)]["currentHub"]["hub"]["date"]["startDate"], "endDate": d["tour"]["items"][str(i)]["currentHub"]["hub"]["date"]["endDate"]}
     
    print(r) 


'''