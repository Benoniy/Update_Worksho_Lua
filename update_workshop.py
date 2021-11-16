#!/usr/bin/env python3

import urllib3
import os
import sys

colID = sys.argv[1]
print("Grabbing collection " + colID  + "...")

url = 'https://steamcommunity.com/sharedfiles/filedetails/?id=' + colID
http = urllib3.PoolManager()
response = http.request('GET', url)
data = str(response.data)


print("Extracting ID's...")

check = '"id":'
list = []

while True:
    string = data[data.find(check):data.find(check) + 18]
    data = data.replace(string, "")
    string = string.replace('"id":"', '')
    string = string.replace('"', '')
    string = string.replace(',', '')
    if string == "":
        break
    list.append(string)

try:
    os.remove("garrysmod/lua/autorun/server/workshop.lua")
    os.remove("garrysmod/lua/autorun/workshop.lua")
except:
    print("Generating workshop.lua...")

fs = open("garrysmod/lua/autorun/server/workshop.lua", "w+")
f = open("garrysmod/lua/autorun/workshop.lua", "w+")

for s in list:
    fs.write('resource.AddWorkshop("' + s + '")\n')
    f.write('resource.AddWorkshop("' + s + '")\n')

fs.close()
f.close()


print("Removing unused .gma's...")
dir = []
path = "garrysmod/cache/srcds/"

for (dirpath, dirnames, filenames) in os.walk(path):
	for name in filenames:
		if ".gma" in name:
			dir.append(name.replace(".gma",""))

remove = set(dir)-set(list)

for f in remove:
	f = f + ".gma"
	print("Removing " + f + "\n")
	os.remove(path + f)
