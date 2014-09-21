from django.http import HttpResponse
from django.template import RequestContext, loader
from util import CollectionSpaceClient
import json

# Create your views here
def browse(request):
    client = CollectionSpaceClient(
        app_id='50090494',
        app_key='2080f7ee22be1e55783f8f9d8b631f82'
    )
    json_data = client.fetch()
    artifacts = client.parse(json_data)

    template = loader.get_template('browseByImage/browse.html')
    context = RequestContext(request, {
        'name': "Robert",
        'data': artifacts
    })
    return HttpResponse(template.render(context))

def detail(request, artifact_id):
    client = CollectionSpaceClient(
        app_id='50090494',
        app_key='2080f7ee22be1e55783f8f9d8b631f82'
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
