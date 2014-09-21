import json
import requests

class CollectionSpaceClient(object):

    def __init__(self, app_id, app_key):
        self.debug = True;
        self.app_id, self.app_key = app_id, app_key
        self.headers = {
            'app_id': app_id,
            'app_key': app_key,
        }
        self.api_url = "https://apis-qa.berkeley.edu/hearst_museum/select"

    def fetch(self, **params):
        queryParams = {
            'q': "objname_s:* AND objfcpgeoloc_p:[-90,-180 TO 90,180] AND blob_ss:[* TO *]",
            'wt': "json",
            'rows': '16',
        }

        response = requests.get(self.api_url, headers = self.headers, params=queryParams)
        if (self.debug):
            print "fetch URL: %s\n\n" % (response.url)
        return json.loads(response.text)

    def parse(self, json_data):
        raw_results = json_data['response']['docs']
        results = []
        for raw_result in raw_results:
            result = {}
            result["name"] = raw_result['objname_s'] if 'objname_s' in raw_result else None
            result["description"] = raw_result['objdescr_s'] if 'objdescr_s' in raw_result else None
            result["artifact_id"] = raw_result['objmusno_s']
            result["geotag"] = raw_result['objfcpgeoloc_p']
            result["image_blob_id"] = raw_result['blob_ss'][0]
            results.append(result)
            if (self.debug):
                print "Raw result: %s\nParsed response: %s\n"% (raw_result, result)

        return results

    def fetch_artifact(self, artifact_id):
        queryParams = {
            'q': "objmusno_s:%s" % artifact_id,
            'wt': "json",
            'rows': '1',
        }

        response = requests.get(self.api_url, headers = self.headers, params=queryParams)
        if (self.debug):
            print "fetch_artifact URL: %s\n\n" % (response.url)
        return json.loads(response.text)

    def fetch_related(self, artifact):
        queryParams = {
            'q': "objname_s:* AND blob_ss:[* TO *]",
            'sfield': "objfcpgeoloc_p",
            'pt': artifact["geotag"],
            'd': "10",
            'sort': "geodist()asc",
            'wt': "json",
            'rows': '5',
            'indent': "on", #DEBUG
        }
        response = requests.get(self.api_url, headers = self.headers, params=queryParams)
        if (self.debug):
            print "fetch_related URL: %s\n\n" % (response.url)
        return json.loads(response.text)

