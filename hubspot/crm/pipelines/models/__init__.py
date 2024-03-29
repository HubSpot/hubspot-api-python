# coding: utf-8

# flake8: noqa
"""
    Pipelines

    Pipelines represent distinct stages in a workflow, like closing a deal or servicing a support ticket. These endpoints provide access to read and modify pipelines in HubSpot. Pipelines support `deals` and `tickets` object types.  ## Pipeline ID validation  When calling endpoints that take pipelineId as a parameter, that ID must correspond to an existing, un-archived pipeline. Otherwise the request will fail with a `404 Not Found` response.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from hubspot.crm.pipelines.models.collection_response_pipeline_no_paging import CollectionResponsePipelineNoPaging
from hubspot.crm.pipelines.models.collection_response_pipeline_stage_no_paging import CollectionResponsePipelineStageNoPaging
from hubspot.crm.pipelines.models.collection_response_public_audit_info_no_paging import CollectionResponsePublicAuditInfoNoPaging
from hubspot.crm.pipelines.models.error import Error
from hubspot.crm.pipelines.models.error_detail import ErrorDetail
from hubspot.crm.pipelines.models.pipeline import Pipeline
from hubspot.crm.pipelines.models.pipeline_input import PipelineInput
from hubspot.crm.pipelines.models.pipeline_patch_input import PipelinePatchInput
from hubspot.crm.pipelines.models.pipeline_stage import PipelineStage
from hubspot.crm.pipelines.models.pipeline_stage_input import PipelineStageInput
from hubspot.crm.pipelines.models.pipeline_stage_patch_input import PipelineStagePatchInput
from hubspot.crm.pipelines.models.public_audit_info import PublicAuditInfo
