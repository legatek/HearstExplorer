from django.http import HttpResponse
from django.template import RequestContext, loader
from util import CollectionSpaceClient
import json

# Create your views here
def browse(request):
    client = CollectionSpaceClient(
        app_id='/*appId goes here*/',
        app_key='/*appKey goes here*/'
    )
    json_data = client.fetch()
    artifacts = client.parse(json_data)

    template = loader.get_template('browseByImage/browse.html')
    context = RequestContext(request, {
        'data': artifacts
    })
    return HttpResponse(template.render(context))

def detail(request, artifact_id):
    client = CollectionSpaceClient(
        app_id='/*appId goes here*/',
        app_key='/*appKey goes here*/'
    )
    json_data = client.fetch_artifact(artifact_id)
    artifacts = client.parse(json_data)

    template = loader.get_template('browseByImage/detail.html')
    related_artifacts=client.parse(client.fetch_related(artifacts[0]))
    context = RequestContext(request, {
        'artifact': artifacts[0],
        'related_artifacts': related_artifacts
    })
    return HttpResponse(template.render(context))

def refinedBrowse(request, keyword):
    client = CollectionSpaceClient(
        app_id='/*appId goes here*/',
        app_key='/*appKey goes here*/'
    )
    json_data = client.fetch(keyword=keyword)
    artifacts = client.parse(json_data)

    template = loader.get_template('browseByImage/refinedBrowse.html')
    context = RequestContext(request, {
        'data': artifacts,
        'keyword': keyword
    })
    return HttpResponse(template.render(context))
