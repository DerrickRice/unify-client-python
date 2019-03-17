import responses

from tamr_unify_client import Client
from tamr_unify_client.auth import UsernamePasswordAuth
from tamr_unify_client.models.project.collection import ProjectCollection


class MyProjectCollection(ProjectCollection):
    def __init__(self, *args, **kwargs):
        self.has_been_streamed = False
        super().__init__(*args, **kwargs)

    def stream(self):
        self.has_been_streamed = True
        return super().stream()


@responses.activate
def test_project_collection():
    class_mapping = {ProjectCollection: MyProjectCollection}

    client = Client(
        UsernamePasswordAuth("username", "password"), class_mapping=class_mapping
    )

    assert isinstance(client.projects, MyProjectCollection)
    assert client.projects.has_been_streamed is not None

    projects_url = "http://localhost:9100/api/versioned/v1/projects"
    responses.add(responses.GET, projects_url, json=[])
    for not_found in client.projects:
        assert False

    assert client.projects.has_been_streamed is True
