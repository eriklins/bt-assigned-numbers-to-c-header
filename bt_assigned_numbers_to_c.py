# bt_assigned_numbers_to_c.py
#
# This Python script converts the files
# - service_uuids.json
# - characteristic_uuids.json
# - descriptor_uuids.json
# - company_ids.json
# into a Pascal unit with constant array definitions for that information.
#
# The original files are available from https://github.com/NordicSemiconductor/bluetooth-numbers-database/tree/master/v1
#
# (C) Erik Lins 2024, (https://github.com/eriklins)

import sys
import re
import json
import yaml
import datetime
import requests
from urllib.request import urlopen

# open again for writing and parse line by line
outfile = open("bt_assigned_numbers.h", "w", encoding="utf-8")

# print header and start of Pascal unit
print("""/* BT SiG Assigned Numbers

   Bluetooth SiG Assigned Numbers for
     - Service UUIDs
     - Characteristic UUIDs
     - Descriptor UUIDs
     - Company IDs
     - GAP Appearance

   Converted from https://github.com/NordicSemiconductor/bluetooth-numbers-database/tree/master/v1
   into a C header file with bt_assigned_numbers_to_c.py Python script.
   """, file=outfile)
print("   "+str(datetime.datetime.now()), file=outfile)
print("""
   bt_assigned_numbers_to_c.py is (C) Erik Lins 2024, (https://github.com/eriklins)

   MIT License
*/

#include <stdint.h>

typedef const struct _uuids_t_ Uuid;
const struct _uuids_t_
{
    const char* uuid;
    const char* name;
    const char* identifier;
};

typedef const struct _company_ids_t_ CompanyIds;
const struct _company_ids_t_
{
    const uint16_t code;
    const char* name;
};

typedef const struct _gap_appearance_t_ GapAppearance;
const struct _gap_appearance_t_
{
    const uint16_t category;
    const char* name;
    const uint8_t value;
    const char* sub_name;
};
""", file=outfile)

# service_uuids.json
url = urlopen("https://raw.githubusercontent.com/NordicSemiconductor/bluetooth-numbers-database/master/v1/service_uuids.json")
data = json.loads(url.read())
print("const int service_uuids_len = "+str(len(data))+";", file=outfile)
print("Uuid service_uuids["+str(len(data))+"] = {", file=outfile)
for idx, i in enumerate(data):
    if len(i['uuid']) == 4:
        print("    {\"0000"+i['uuid'].lower()+"-0000-1000-8000-00805f9b34fb\", \""+i['name']+"\", \""+i['identifier']+"\"}", end="", file=outfile)
    elif len(i['uuid']) == 8:
        print("    {\""+i['uuid'].lower()+"-0000-1000-8000-00805f9b34fb\", \""+i['name']+"\", \""+i['identifier']+"\"}", end="", file=outfile)
    else:
        print("    {\""+i['uuid'].lower()+"\", \""+i['name']+"\", \""+i['identifier']+"\"}", end="", file=outfile)
    if idx < (len(data)-1):
        print(",", file=outfile)
print("", file=outfile)
print("};", file=outfile)
print("", file=outfile)

# characteristic_uuids.json
url = urlopen("https://raw.githubusercontent.com/NordicSemiconductor/bluetooth-numbers-database/master/v1/characteristic_uuids.json")
data = json.loads(url.read())
print("const int characteristic_uuids_len = "+str(len(data))+";", file=outfile)
print("Uuid characteristic_uuids["+str(len(data))+"] = {", file=outfile)
for idx, i in enumerate(data):
    if len(i['uuid']) == 4:
        print("    {\"0000"+i['uuid'].lower()+"-0000-1000-8000-00805f9b34fb\", \""+i['name']+"\", \""+i['identifier']+"\"}", end="", file=outfile)
    elif len(i['uuid']) == 8:
        print("    {\""+i['uuid'].lower()+"-0000-1000-8000-00805f9b34fb\", \""+i['name']+"\", \""+i['identifier']+"\"}", end="", file=outfile)
    else:
        print("    {\""+i['uuid'].lower()+"\", \""+i['name']+"\", \""+i['identifier']+"\"}", end="", file=outfile)
    if idx < (len(data)-1):
        print(",", file=outfile)
print("", file=outfile)
print("};", file=outfile)
print("", file=outfile)

# descriptor_uuids.json
url = urlopen("https://raw.githubusercontent.com/NordicSemiconductor/bluetooth-numbers-database/master/v1/descriptor_uuids.json")
data = json.loads(url.read())
print("const int descriptor_uuids_len = "+str(len(data))+";", file=outfile)
print("Uuid descriptor_uuids["+str(len(data))+"] = {", file=outfile)
for idx, i in enumerate(data):
    if len(i['uuid']) == 4:
        print("    {\"0000"+i['uuid'].lower()+"-0000-1000-8000-00805f9b34fb\", \""+i['name']+"\", \""+i['identifier']+"\"}", end="", file=outfile)
    elif len(i['uuid']) == 8:
        print("    {\""+i['uuid'].lower()+"-0000-1000-8000-00805f9b34fb\", \""+i['name']+"\", \""+i['identifier']+"\"}", end="", file=outfile)
    else:
        print("    {\""+i['uuid'].lower()+"\", \""+i['name']+"\", \""+i['identifier']+"\"}", end="", file=outfile)
    if idx < (len(data)-1):
        print(",", file=outfile)
print("", file=outfile)
print("};", file=outfile)
print("", file=outfile)

# company_ids.json
url = urlopen("https://raw.githubusercontent.com/NordicSemiconductor/bluetooth-numbers-database/master/v1/company_ids.json")
data = json.loads(url.read())
print("const int company_identifier_len = "+str(len(data))+";", file=outfile)
print("CompanyIds company_identifier["+str(len(data))+"] = {", file=outfile)
for idx, i in enumerate(data):
    print("    {"+str(i['code'])+", \""+i['name'].replace('"', '\\"')+"\"}", end="", file=outfile)
    if idx < (len(data)-1):
        print(",", file=outfile)
print("", file=outfile)
print("};", file=outfile)
print("", file=outfile)

# gap_appearance.json
url = urlopen("https://raw.githubusercontent.com/NordicSemiconductor/bluetooth-numbers-database/master/v1/gap_appearance.json")
data = json.loads(url.read())
l = 0
for idx, i in enumerate(data):
    if "subcategory" not in i:
        l += 1
    else:
        for vdx, v in enumerate(i['subcategory']):
            l += 1
print("const int gap_appearance_len = "+str(l)+";", file=outfile)
print("GapAppearance gap_appearance["+str(l)+"] = {", file=outfile)
for idx, i in enumerate(data):
    if "subcategory" not in i:
        print("    {"+str(i['category'])+", \""+i['name']+"\", 0, \"\"}", end="", file=outfile)
    else:
        for vdx, v in enumerate(i['subcategory']):
            print("    {"+str(i['category'])+", \""+i['name']+"\", "+str(v['value'])+", \""+v['name']+"\"}", end="", file=outfile)
            if vdx < (len(i['subcategory'])-1):
                print(",", file=outfile)
        if vdx < (len(i['subcategory'])-1):
            print(",", file=outfile)
    if idx < (len(data)-1):
        print(",", file=outfile)
print("", file=outfile)
print("};", file=outfile)
print("", file=outfile)

# close output file
outfile.close()

