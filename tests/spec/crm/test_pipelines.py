import hubspot
from hubspot.crm.pipelines import PipelinesApi, PipelineStagesApi


def test_is_discoverable():
    apis = hubspot.Client.create().crm.pipelines
    assert isinstance(apis.pipelines_api, PipelinesApi)
    assert isinstance(apis.pipeline_stages_api, PipelineStagesApi)
