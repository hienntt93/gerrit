# Step 1 (wait for enhancement)
# using existinct cookie for logging on)

import requests

url = "https://gerrit-url/projects/"

headers = {'Cookie':'cookie-value'}

params = {'n':{the maximum number},'S':{the starting number},'query':'value-for-searching'}

result = requests.request('GET',url=url, params=params,headers=headers)
==========================================================================
==========================================================================

# Step 2 get the response as raw date before processing

import json
json_data = json.loads(result.text[5:])
print(json_data)

==========================================================================
==========================================================================

# Step 3 define needed fields then write them into a csv file

import csv
f = open('output_data.csv','w',newline='')
columns = [{some columns name in here}]
# writer = csv.writer(f, delimiter = ' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
writer = csv.DictWriter(f, fieldnames=columns)
writer.writeheader()
for i in json_data:
   
    writer.writerow({'id':i['id'],'name':i['name'], 'state': i['state'], 'url': i['web_links'][0]['url']})

f.close()
