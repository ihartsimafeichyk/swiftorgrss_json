
import wget
import xmltodict
import json
import os

os.remove('atom.xml')
# Download file
print('---> Beginning file download with wget module')
url = 'https://swift.org/atom.xml'
wget.download(url)

with open('atom.xml') as xml:
	my_dict=xmltodict.parse(xml.read())
json_data=json.dumps(my_dict)
print(json_data)