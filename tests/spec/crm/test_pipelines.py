from hubspot import HubSpot
from hubspot.crm.pipelines import (
    PipelinesApi,
    PipelineStagesApi,
    PipelineAuditsApi,
    PipelineStageAuditsApi
)


def test_is_discoverable():
    apis = HubSpot().crm.pipelines
    assert isinstance(apis.pipelines_api, PipelinesApi)
    assert isinstance(apis.pipeline_stages_api, PipelineStagesApi)
    assert isinstance(apis.pipelines_audits_api, PipelineAuditsApi)
    assert isinstance(apis.pipelines_stage_audits_api, PipelineStageAuditsApi)
