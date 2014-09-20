import json
import requests

class CollectionSpaceClient(object):
    def __init__(self, app_id, app_key):
        self.app_id, self.app_key = app_id, app_key
        self.headers = {
            'app_id': app_id,
            'app_key': app_key,
        }
        self.api_url = "https://apis-qa.berkeley.edu/hearst_museum/select"

    def fetch(self, **params):
        queryParams = {
            'q': "objname_s:headdress",
            'wt': "json",
            'rows': '3',
            'indent': "on", #DEBUG
        }

        response = requests.get(self.api_url, headers = self.headers, params=queryParams)
        print response.text
        return json.loads(response.text)

    def parse(self, json_data):
        raw_results = json_data['response']['docs']
        results = []
        for raw_result in raw_results:
            result = {}
            result["name"] = raw_result['objname_s'] if 'objname_s' in raw_result else None
            result["description"] = raw_result['objdescr_s'] if 'objdescr_s' in raw_result else None
            result["artifact_id"] = raw_result['id']
            results.append(result)

        return results