import json
import requests
import random

class CollectionSpaceClient(object):

    def __init__(self, app_id, app_key):
        self.debug = True;
        self.app_id, self.app_key = app_id, app_key
        self.headers = {
            'app_id': app_id,
            'app_key': app_key,
        }
        self.api_url = "https://apis-qa.berkeley.edu/hearst_museum/select"
        self.MAX_NUM_BROWSE_ITEMS = 2000 #Grab additional results to shuffle and randomize the result set
        self.SELECT_NUM_BROWSE_ITEMS = 25
        self.MAX_NUM_RELATED_ITEMS = 50
        self.SELECT_NUM_RELATED_ITEMS = 5

    def fetch(self, keyword=None, **params):
        queryParams = {
            'q': "objname_s:* AND objfcpgeoloc_p:[-90,-180 TO 90,180] AND blob_ss:[* TO *]",
            'wt': "json",
            'rows': self.MAX_NUM_BROWSE_ITEMS,
        }

        if (keyword != None):
            queryParams['q'] = "objname_s:* AND objfcpgeoloc_p:[-90,-180 TO 90,180] AND blob_ss:[* TO *] and text:%s" % keyword,

        response = requests.get(self.api_url, headers = self.headers, params=queryParams)
        if (self.debug):
            print "fetch URL: %s\n\n" % (response.url)

        return self.shuffle_results(response.text, self.SELECT_NUM_BROWSE_ITEMS)

    def shuffle_results(self, response_text, num_results):
        data = json.loads(response_text)
        artifact_data = data['response']['docs']
        random.shuffle(artifact_data)
        return artifact_data[1:num_results+1] #Non-inclusive

    def parse(self, json_data):
        results = []
        for raw_result in json_data:
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

        data = json.loads(response.text)
        return data['response']['docs']

    def fetch_related(self, artifact):
        queryParams = {
            'q': "objname_s:* AND objfcpgeoloc_p:[-90,-180 TO 90,180] AND blob_ss:[* TO *]",
            'sfield': "objfcpgeoloc_p",
            'pt': artifact["geotag"],
            'd': "100",
            'sort': "geodist()asc",
            'wt': "json",
            'rows': self.MAX_NUM_RELATED_ITEMS,
            'indent': "on", #DEBUG
        }
        response = requests.get(self.api_url, headers = self.headers, params=queryParams)
        if (self.debug):
            print "fetch_related URL: %s\n\n" % (response.url)
        return self.shuffle_results(response.text, self.SELECT_NUM_RELATED_ITEMS)

