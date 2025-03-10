import hubspot.crm.pipelines as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):

    @property
    def pipeline_audits_api(self) -> api_client.PipelineAuditsApi:
        return self._configure_api_client(api_client, "PipelineAuditsApi")

    @property
    def pipeline_stage_audits_api(self) -> api_client.PipelineStageAuditsApi:
        return self._configure_api_client(api_client, "PipelineStageAuditsApi")

    @property
    def pipeline_stages_api(self) -> api_client.PipelineStagesApi:
        return self._configure_api_client(api_client, "PipelineStagesApi")

    @property
    def pipelines_api(self) -> api_client.PipelinesApi:
        return self._configure_api_client(api_client, "PipelinesApi")
