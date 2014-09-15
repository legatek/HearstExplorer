import requests
import json

url = 'https://apis-qa.berkeley.edu/hearst_museum/select'
headers = {}
headers['app_key'] = "2080f7ee22be1e55783f8f9d8b631f82"
headers['app_id'] = "50090494"

#q=objdescr_s%3Asandal&wt=json&indent=on
params = {
#'q': 'objculturetree_txt:Arctic',
'q': 'objmaterials_txt:gold',
#'q': 'objdescr_s:headdress',
'wt': 'json',
'indent': True,
#'facet': 'true',
#'facet.field':'objculturetree_ss'
}
r = requests.get(url, params=params, headers=headers)

print r.url
print r.status_code
print json.dumps(json.loads(r.text), indent=4)
