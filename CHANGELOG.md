# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased](https://github.com/HubSpot/hubspot-api-python/compare/v12.0.0-beta.2...HEAD)

## [12.0.0-beta.2](https://github.com/HubSpot/hubspot-api-python/compare/v12.0.0-beta.1...v12.0.0-beta.2) - 2025-05-07

## Files

- Changed incomining parameters list in `files.files_api.do_search()`.
- Renamed method `archive_gdpr()` to `delete()` in `files.files_api`.
- Renamed method `update_properties()` to `update_properties_recursively()` in `files.folders_api`.
- Added new method `update_properties()` to `files.folders_api`.
- Changed incomining parameters list in `files.folders_api.do_search()`.
- Added properties `source_group` and `file_md5` to `File`.
- Added property `clear_expires` to `FileUpdateInput`.
- Changed property type from `"expires_at": "int"` to `"expires_at": "datetime"` in `FileUpdateInput`.
- Added property `expires_at` to `ImportFromUrlInput`.
- Removed property `id` from `FolderUpdateInput`.

## Other changes

- Added parameter `object_write_trace_id` to models: `simple_public_object`, `simple_public_object_with_associations`, `simple_public_upsert_object` for  `crm.products`, `crm.objects.goals`, `crm.tickets`.
- Removed parameter `object_write_trace_id` from models: `simple_public_object_input`, `simple_public_object_input_for_create` for  `crm.products`, `crm.objects.goals`, `crm.tickets`.
- Added method `merge()` to `crm.tickets.basic_api`.
- Removed `crm.tickets.merge_api` Api.
- Marked `CMS Performance` as deprecated.

## [12.0.0-beta.1](https://github.com/HubSpot/hubspot-api-python/compare/v11.1.0...v12.0.0-beta.1) - 2025-04-16

## CRM Objects

- Renamed `BatchInputSimplePublicObjectInputForCreate` to `BatchInputSimplePublicObjectBatchInputForCreate` for `crm.contacts`, `crm.companies`, `crm.deals`, `crm.objects`, `crm.objects.taxes`, `crm.objects.tasks`, `crm.objects.postal_mail`, `crm.objects.notes`, `crm.objects.meetings`, `crm.objects.leads`, `crm.objects.emails`, `crm.objects.communications`, `crm.objects.line_items`, `crm.objects.quotes`, `crm.objects.calls`.
- Removed methods `archive()`, `create()` and `update()` from `crm.objects.feedback_submissions.basic_api`.
- Removed methods `archive()`, `create()` and `update()` from `crm.objects.feedback_submissions.batch_api`.
- Added parameters `uses_remote` and `uses_calling_window` to `crm.extensions.calling.models.settings_patch_request`, `crm.extensions.calling.models.settings_request` and `crm.extensions.calling.models.settings_response`.
- Added parameter `object_write_trace_id` to models: `simple_public_object`, `simple_public_object_with_associations`, `simple_public_upsert_object` for `crm.contacts`, `crm.companies`, `crm.deals`, `crm.objects`, `crm.objects.taxes`, `crm.objects.tasks`, `crm.objects.postal_mail`, `crm.objects.notes`, `crm.objects.meetings`, `crm.objects.leads`, `crm.objects.emails`, `crm.objects.communications`, `crm.objects.line_items`, `crm.objects.quotes`, `crm.objects.calls`.
- Removed parameter `object_write_trace_id` from models: `simple_public_object_input`, `simple_public_object_input_for_create` for `crm.contacts`, `crm.companies`, `crm.deals`, `crm.objects`, `crm.objects.taxes`, `crm.objects.tasks`, `crm.objects.postal_mail`, `crm.objects.notes`, `crm.objects.meetings`, `crm.objects.leads`, `crm.objects.emails`, `crm.objects.communications`, `crm.objects.line_items`, `crm.objects.quotes`, `crm.objects.calls`.

## CRM Extensions, Imports and Owners

- Added parameters `uses_remote` and `uses_calling_window` to `crm.extensions.calling.models.settings_patch_request`, `crm.extensions.calling.models.settings_request` and `crm.extensions.calling.models.settings_response`.
- Added parameters `include_error_message` and `include_row_data` to `crm.imports.public_imports_api`.
- Added parameter `contains_encrypted_properties` to `crm.imports.models.import_row_core`.
- Added parameters `invalid_property_value`, `error_message` and `invalid_value_to_display` to `crm.imports.models.public_import_error`.
- Added parameter `mapped_object_type_ids` to `crm.imports.models.public_import_response`.
- Added parameter `user_id_including_inactive` and `type` to `crm.owners.models.public_owner`.

## Marketing

- Added parameter `object_id` to `marketing.events.models.marketing_event_default_response`, `marketing.events.models.marketing_event_default_response` and `marketing.events.models.marketing_event_public_read_response`.
- Added methods `archive_by_object_id()`, `get_all()`, `get_by_object_id()` and `update_by_object_id()` to `marketing.events.basic_api`.
- Renamed from `marketing.transactional.api.PublicSmtpTokensApi` to `marketing.transactional.api.PublicSMTPTokensApi`.
- Renamed from `marketing.events.participant_state_api` to `marketing.events.retrieve_participant_state_api`.
- Renamed from `CollectionResponseMarketingEventExternalUniqueIdentifierNoPaging` to `CollectionResponseSearchPublicResponseWrapperNoPaging`.
- Moved and renamed methods from `basic_api.batch_archive()` and `basic_api.batch_upsert()` to `batch_api.archive()` and `batch_api.upsert()`.
- Moved methods from `basic_api.compelte()` and `basic_api.cancel()` to `change_property_api.compelte()` and `change_property_api.cancel()`.
- Moved method from `basic_api.do_search()` to `identifiers_api.do_search()`.

## Webhooks

- Added parameter `object_type_id` to `webhooks.models.subscription_create_request` and `webhooks.models.subscription_response`.
- Removed parameter `period` from `webhooks.models.throttling_settings`.

## Added new Client APIs

- `crm.companies.merge_api` Api.
- `crm.extensions.calling.channel_connection_settings_api` Api.
- `marketing.events.add_event_attendees_api` Api.
- `marketing.events.batch_api` Api.
- `marketing.events.change_property_api` Api.
- `marketing.events.identifiers_api` Api.
- `cms.blogs.blog_posts.basic_api` Api.
- `cms.blogs.blog_posts.batch_api` Api.
- `cms.blogs.blog_posts.multi_language_api` Api.
- `events.send.basic_api` Api.
- `events.send.batch_api` Api.

## Removed Client APIs

- `cms.blogs.blog_posts.blog_posts_api` Api.
- `marketing.events.attendance_subscriber_state_changes_api` Api.
- `crm.objects.feedback_submissions.gdpr_api` Api.
- `crm.objects.feedback_submissions.public_object_api` Api.
- `crm.companies.merge_api` Api.
- `crm.contacts.merge_api` Api.
- `crm.deals.merge_api` Api.
- `crm.contacts.gdpr_api` Api.
- `events.send.custom_event_data_api` Api.
- `events.send.default_api` Api.

## Added new Clients

- `Marketing Emails` client.
- `Invoices` client.
- `Exports` client.
- `Deal Splits` client.

## Other updates

- Updated `README`.
- Fixed urlencoding `query_string` for `api_request`.

## [11.1.0](https://github.com/HubSpot/hubspot-api-python/compare/v11.0.0...v11.1.0) - 2024-12-23

## Fix

- Signature compatibility with python <3.11.
- Wrong change definition at 9.0.0 changelog.
- Urllib3 requirements.

## [11.0.0](https://github.com/HubSpot/hubspot-api-python/compare/v10.0.0...v11.0.0) - 2024-11-27

## Associations

- Added `assiciations.v4.report_api` Api.
- Added `assiciations.v4.schema.definition_configurations_api` Api.

## Marketing Events

- Added `marketing.events.list_associations_api` Api.
- Renamed method `create_by_contact_email` to `record_by_contact_emails` in `marketing.events.attendance_subscriber_state_changes_api`.
- Renamed method `create_by_contact_id` to `record_by_contact_ids` in `marketing.events.attendance_subscriber_state_changes_api`.
- Remove parameters `attendance_state_calculation_timestamp` and `import_status` to `marketing.events.models.marketing_event_update_request_params`.

## Other changes

- Added `api_request` Api(for requests by curl).
- Enhance `get_all` method.
- Added possibility change all configuration params("proxy", "proxy_headers" and ect.).
- Fix call `crm.tickets.merge_api`.
- Update README.
- Update requires.
- Update Makefile.

## [10.0.0](https://github.com/HubSpot/hubspot-api-python/compare/v9.0.0...v10.0.0) - 2024-10-10

## CMS

- Added parameter `campaign_name` to `cms.blogs.blog_posts.models.content_language_variation`.
- Added parameter `breakpoint_styles` to `cms.blogs.blog_posts.models.styles`.
- Added parameter `name` to `cms.hubdb.rows_api.clone_draft_table_row()`.
- Added parameter `archived` to `cms.hubdb.rows_api.get_draft_table_row_by_id()` and `cms.hubdb.rows_api.get_table_row()`.
- Added parameters `offset` and `archived` to `cms.hubdb.rows_api.get_table_rows()` and `cms.hubdb.rows_api.read_draft_table_rows()`.
- Added parameter `content_type` parameter to `cms.hubdb.tables_api.export_table()` and `cms.hubdb.tables_api.get_all_tables()`.
- Added parameter `is_get_localized_schema` parameter to `cms.hubdb.tables_api.get_draft_table_details_by_id()`, `cms.hubdb.tables_api.get_table_details()` and `cms.hubdb.tables_api.update_draft_table()`.
- Added parameters `created_by_user_id`, `updated_by`, `updated_by_user_id`, `created_at`, `created_by` and `updated_at` to `cms.hubdb.models.column` and `cms.hubdb.models.option`.
- Added parameter `is_hubspot_defined` to `cms.hubdb.models.hub_db_table_clone_request`.
- Added `do_async()` and `get_async_status()` methods to `cms.source_code.extract_api`.
- Changed the response object type from  `CollectionResponseWithTotalHubDbTableRowV3ForwardPaging` to `UnifiedCollectionResponseWithTotalBaseHubDbTableRowV3` for `cms.hubdb.rows_api.get_table_rows()` and `cms.hubdb.rows_api.read_draft_table_rows()`.
- Changed parameter `batch_input_string: BatchInputString` to `batch_input_hub_db_table_row_batch_clone_request: BatchInputHubDbTableRowBatchCloneRequest` in `cms.hubdb.rows_api.clone_draft_table_row()`.
- Updated `language` validation: Added a predefined list of `allowed_values` for stricter validation for `cms.blogs.blog_posts.models.attach_to_lang_primary_request_v_next`.
- Updated `type` validation: Expanded `allowed_values` for validation for `cms.hubdb.models.column_request`.
- Removed `cms.source_code.extract_api.extract_by_path()` method.
- Removed `cms.source_code.source_code_extract_api`.

## CRM

- Added `crm.objects.leads` Api client.
- Added method `upsert` to `crm.companies.batch_api`, `crm.contacts.batch_api`, `crm.deals.batch_api`, `crm.line_items.batch_api`, `crm.objects.batch_api`, `crm.objects.calls.batch_api`, `crm.objects.communications.batch_api`, `crm.objects.emails.batch_api`, `crm.objects.meetings.batch_api`, `crm.objects.notes.batch_api`, `crm.objects.postal_mail.batch_api`, `crm.objects.tasks.batch_api`, `crm.objects.taxes.batch_api`, `crm.products.batch_api`, `crm.quotes.batch_api`, `crm.tickets.batch_api`.
- Added parameter `object_write_trace_id` to models: `simple_public_object_input`, `simple_public_object_batch_input`, `simple_public_object_input_for_create` for `crm.companies`, `crm.contacts`, `crm.deals`, `crm.line_items`, `crm.objects`, `crm.objects.calls`, `crm.objects.communications`, `crm.objects.emails`, `crm.objects.meetings`, `crm.objects.notes`, `crm.objects.postal_mail`, `crm.objects.tasks`, `crm.objects.taxes`, `crm.products`, `crm.quotes`, `crm.tickets`.
- Added method `mark_as_ready()` to `crm.extensions.calling.recording_settings_api`.
- Added parameters `created_by_user_id` and `updated_by_user_id` to `crm.schemas.models.object_schema`.
- Added parameter `clear_description` to `crm.schemas.models.object_type_definition_patch`.
- Added parameter `supports_inbound_calling` to `crm.extensions.calling.models.settings_patch_request`, `crm.extensions.calling.models.settings_request` and `crm.extensions.calling.models.settings_response`.
- Changed `association_category` and `association_type_id` parameters can be `None` in `crm.companies.models.association_spec`, `crm.contacts.models.association_spec`, `crm.deals.models.association_spec`, `crm.tickets.models.association_spec`.
- Changed `types` and `to` parameters can be `None` in `crm.companies.models.public_associations_for_object`, `crm.contacts.models.public_associations_for_object`, `crm.deals.models.public_associations_for_object`, and `crm.tickets.models.public_associations_for_object`.
- Changed `id` parameters can be `None` in `crm.companies.models.public_object_id`, `crm.contacts.models.public_object_id`, `crm.deals.models.public_object_id`, and `crm.tickets.models.public_object_id`.
- Changed `limit`, `after`, `sorts`, `properties`, and `filter_groups` parameters can be `None` in `crm.companies.models.public_object_search_request`, `crm.contacts.models.public_object_search_request`, `crm.deals.models.public_object_search_request`, `crm.line_items.models.public_object_search_request`, `crm.objects.models.public_object_search_request`, `crm.objects.calls.models.public_object_search_request`, `crm.objects.communications.models.public_object_search_request`, `crm.objects.emails.models.public_object_search_request`, `crm.objects.goals.models.public_object_search_request`, `crm.objects.postal_mail.models.public_object_search_request`, `crm.objects.tasks.models.public_object_search_request`, `crm.objects.taxes.models.public_object_search_request`, `crm.products.models.public_object_search_request`, `crm.quotes.models.public_object_search_request`, and `crm.tickets.models.public_object_search_request`.
- Changed `associations` parameters can be `None` in `crm.companies.models.simple_public_object_input_for_create`, `crm.contacts.models.simple_public_object_input_for_create`, `crm.deals.models.simple_public_object_input_for_create`, and `crm.tickets.models.simple_public_object_input_for_create`.
- Renamed `public_object_api` to `merge_api` in `crm.companies`, `crm.contacts`, `crm.deals` and `crm.tickets`.
- Removed `archive`, `create` and `update` methods from `crm.objects.goals.basic_api` and `crm.objects.goals.batch_api`.
- Removed GDPRApi:
`crm.companies.gdpr_api`, `crm.deals.gdpr_api`, `crm.line_items.gdpr_api`, `crm.objects.gdpr_api`, `crm.objects.calls.gdpr_api`, `crm.objects.communications.gdpr_api`, `crm.objects.emails.gdpr_api`, `crm.objects.goals.gdpr_api`, `crm.objects.meetings.gdpr_api`, `crm.objects.notes.gdpr_api`, `crm.objects.postal_mail.gdpr_api`, `crm.objects.tasks.gdpr_api`, `crm.objects.taxes.gdpr_api`, `crm.products.gdpr_api`, `crm.quotes.gdpr_api`, `crm.tickets.gdpr_api`.
- Removed PublicObjectApi:
`crm.line_items.public_object_api`, `crm.objects.public_object_api`, `crm.objects.calls.public_object_api`, `crm.objects.communications.public_object_api`, `crm.objects.emails.public_object_api`, `crm.objects.goals.public_object_api`, `crm.objects.meetings.public_object_api`, `crm.objects.notes.public_object_api`, `crm.objects.postal_mail.public_object_api`, `crm.objects.tasks.public_object_api`, `crm.objects.taxes.public_object_api`, `crm.products.public_object_api`, `crm.quotes.public_object_api`.
- Removed `crm.schemas.public_object_schemas_api`.
- Removed `crm.extensions.accounting` API client.

## CRM Lists

- Added `crm.objects.lists.folders_api` Api.
- Added `crm.lists.mapping_api` Api.
- Added `crm.lists.memberships_api.get_lists()` and `crm.lists.memberships_api.get_page_ordered_by_added_to_list_date()`.
- Added parameter `custom_properties` to `crm.lists.models.list_create_request`.
- Added parameters `list_ids`, `processing_types` and `sort` to `crm.lists.models.list_search_request`.
- Added parameters `coalescing_refine_by` to `crm.lists.models.public_unified_events_filter_branch`.
- Changed response object type `CollectionResponseLong` to `ApiCollectionResponseJoinTimeAndRecordId` of `crm.lists.membershipsApi.get_page()`.
- Changed `offset` and `additional_properties` parameters can be `None` in `crm.lists.models.list_search_request`.
- Rename model from `PublicEventAnalyticsFilterCoalescingRefineBy` to `PublicFormSubmissionFilterCoalescingRefineBy`.
- Rename model from `PublicPropertyFilterOperation` to `PublicSurveyMonkeyValueFilterValueComparison`.
- Renamed Api client from `crm.lists.list_app_membership_api` to `crm.lists.memberships_api`.
- Renamed Api client from `crm.lists.list_app_api` to `crm.lists.lists_api`.

## Marketing

- Added `marketing.events.participant_state_api` Api.
- Added new methods `batch_archive`, `batch_upsert`, `cancel` and `complete` to `marketing.events.basic_api`.
- Added parameter `event_completed` to `marketing.events.models.marketing_event_public_default_response`,`marketing.events.models.marketing_event_create_request_params`, `marketing.events.models.marketing_event_default_response`, `marketing.events.models.marketing_event_public_read_response`.
- Added parameters `attendance_state_calculation_timestamp`, `event_completed` and `import_status` to `marketing.events.models.marketing_event_update_request_params`.
- Added parameters `data_sensitivity`, `unit` and `is_encrypted` to `marketing.events.models.property_value`.
- Updated `source` validation: Expanded `allowed_values` for validation for `marketing.events.models.property_value`.
- Renamed method `create` to `create_by_contact_id` in `marketing.events.attendance_subscriber_state_changes_api`.
- Renamed method `create_by_email` to `create_by_contact_email` in `marketing.events.attendance_subscriber_state_changes_api`.
- Renamed method `get_by_id` to `get_details` in `marketing.events.basic_api`.
- Renamed method `replace` to `upsert` in `marketing.events.basic_api`.
- Renamed method `create` to `update` in `marketing.events.settings_api`.
- Renamed method `do_email_upsert_by_id` to `upsert_by_contact_email` in `marketing.events.subscriber_state_changes_api`.
- Renamed method `do_upsert_by_id` to `upsert_by_contact_id` in `marketing.events.subscriber_state_changes_api`.
- Moved method `do_search` from `marketing.events.search_api` to `marketing.events.basic_api`.
- Removed `marketing.events.batch_api`.
- Removed `marketing.events.marketing_events_external_api`.
- Removed `marketing.events.search_api`.

## Events and OAuth

- Added `events.api.default_api` Api.
- Moved client from `auth.oauth` to `oauth`.

## Signature

- Fix `MAX_ALLOWED_TIMESTAMP`.
- Changed `timestamp` form `float` to `str`.

## Pkg_resources

- remove deprecated `pkg_resources`.

## [9.0.0](https://github.com/HubSpot/hubspot-api-python/compare/v8.2.1...v9.0.0) - 2024-03-14

### Automation Actions client

- Updated `automation.actions.definitions_api.create()` method to accept `public_action_definition_egg` instead of `extension_action_definition_input` and returned `PublicActionDefinition` instead `ExtensionActionDefinition`.
- Updated `automation.actions.definitions_api.get_by_id()` method to return `PublicActionDefinition` instead of `ExtensionActionDefinition`.
- Updated `automation.actions.definitions_api.get_page()` method to return `CollectionResponsePublicActionDefinitionForwardPaging` instead of `CollectionResponseExtensionActionDefinitionForwardPaging`.
- Updated `automation.actions.definitions_api.update()` method to accept `public_action_definition_patch` instead of `extension_action_definition_patch` and returned `PublicActionDefinition` instead `ExtensionActionDefinition`.
- Updated `automation.actions.functions_api.create_or_replace()` method to return `PublicActionFunctionIdentifier` instead of `ActionFunctionIdentifier`.
- Updated `automation.actions.functions_api.create_or_replace_by_function_type()` method to return `PublicActionFunctionIdentifier` instead of `ActionFunctionIdentifier`.
- Updated `automation.actions.functions_api.get_by_function_type()` method to return `PublicActionFunction` instead of `ActionFunction`.
- Updated `automation.actions.functions_api.get_by_id()` method to return `PublicActionFunction` instead of `ActionFunction`.
- Updated `automation.actions.functions_api.get_page()` method to return `CollectionResponsePublicActionFunctionIdentifierNoPaging` instead of `CollectionResponseActionFunctionIdentifierNoPaging`.
- Updated `automation.actions.revisions_api.get_by_id()` method to return `PublicActionRevision` instead of `ActionRevision`.
- Updated `automation.actions.revisions_api.get_page()` method to return `CollectionResponsePublicActionRevisionForwardPaging` instead of `CollectionResponseActionRevisionForwardPaging`.
- Added new function type `POST_ACTION_EXECUTION` to `automation.actions.models.PublicActionFunctionIdentifier` and `automation.actions.models.PublicActionFunction`.
- Added new param `automation_field_type` to `automation.actions.models.InputFieldDefinition`.
- Added `automation.actions.models.OutputFieldDefinition`.
- Added `automation.actions.models.PublicExecutionTranslationRule`.
- Added new params to `automation.actions.models.FieldTypeDefinition`:

```python
{
  "help_text": "str",
  "referenced_object_type": "str",
  "name": "str",
  "options": "list[Option]",
  "description": "str",
  "external_options_reference_type": "str",
  "label": "str",
  "type": "str",
  "field_type": "str",
  "options_url": "str",
  "external_options": "bool",
}
```

### CMS clients

- Changed `attach_to_lang_group()`, `detach_from_lang_group()` and `update_langs()` methods of all Api clients(`cms.blogs.authors.blog_authors_api`, `cms.blogs.blog_posts.blog_posts_api` and `cms.blogs.tags.blog_tags_api`) return `None` instead of `Error`.
- Added new param `_property` to `cms.blogs.authors.blog_authors_api.get_by_id()` and `cms.blogs.authors.blog_authors_api.get_page()`.
- Renamed `cms.source_code.content_api.get()` method to `cms.source_code.content_api.download()`.
- Renamed `cms.source_code.content_api.replace()` method to `cms.source_code.content_api.create_or_update()`.
- Added new param `hash` to `cms.source_code.models.AssetFileMetadata`.
- Added new param `properties` to `cms.source_code.metadata_api.get()`.

### CRM Associations and Objects clients

> [!NOTE]
> Please note that CRM Objects includes: companies, contacts, deals, line items, all CRM objects `crm.objects`, products, quotes and tickets

- Changed the type of parameter `category` from `ErrorCategory` to `string` in `crm.associations.models.StandardError`.
- Renamed `crm.associations.v4.schema.definitions_api.delete()` method to `crm.associations.v4.schema.definitions_api.archive()`.
- Changed the type of parameters `object_id` and `crm.associations.v4.basic_api.to_object_id` in `crm.associations.v4.basic_api.archive()`, `crm.associations.v4.basic_api.create()` and `crm.associations.v4.basic_api.create_default()` methods from `int` to `string`.
- Changed the type of parameter `object_id` in `crm.associations.v4.basic_api.get_page()` method from `int` to `string`.
- Changed the type of parameters `to_object_id` and `from_object_id` in `crm.associations.v4.models.LabelsBetweenObjectPair` to `string`.
- Changed the type of parameter `to_object_id` in `crm.associations.v4.models.MultiAssociatedObjectWithLabel` to `string`.
- Changed the type of property `category` in `ErrorCategory` to `string` in `crm.associations.v4.models.StandardError`.
- Changed the type of property `errors` in `crm.associations.v4.models.BatchResponsePublicDefaultAssociation` from `StandardError1[]` to `StandardError[]`.
- Added parameter `inverse_label` to `crm.associations.v4.models.PublicAssociationDefinitionCreateRequest` and `crm.associations.v4.models.PublicAssociationDefinitionUpdateRequest`.
- Updated `crm.time_line.events_api.create_batch()` method to return `None` insted `BatchResponseTimelineEventResponse`.
- Changed the type of parameter `category` from `ErrorCategory` to `string` in `crm.time_line.models.StandardError`.
- Removed `crm.objects.associations_api`.
- Renamed param `postal_mail` to `postal_mail_id` in `crm.objects.postal_mail.basic_api()`.
- Changed the type of parameter `after` from `int` to `string` in all CRM models `PublicObjectSearchRequest`.
- Added new param `id_property` in all CRM models `SimplePublicObjectBatchInput`.

### CRM Extensions client

- Changed parameter order in `crm.extinsions.cards_api.archive()` method from `(app_id, card_id)` to `(card_id, app_id)`.
- Updated `crm.extinsions.cards_api.create()` method to return `PublicCardResponse` instead `CardResponse`.
- Updated `crm.extinsions.cards_api.get_all()` method to return `PublicCardListResponse` instead `CardListResponse`.
- Changed parameter order in `crm.extinsions.cards_api.get_by_id()` method from `(app_id, card_id)` to `(card_id, app_id)` and method return `PublicCardResponse` instead `CardResponse`.
- Changed parameter order in `crm.extinsions.cards_api.update()` method from `(app_id, card_id, card_patch_request)` to `(card_id, app_id, card_patch_request)` and method return `PublicCardResponse` instead `CardResponse`.
- Added new params `serverless_function` and `card_type` to `crm.extinsions.models.CardFetchBody` and `crm.extinsions.models.CardFetchBodyPatch`.
- Added new param `audit_history` to `crm.extinsions.models.PublicCardResponse`.
- Added new allowable value `marketing_events` to `crm.extinsions.models.CardObjectTypeBody`.
- Added `developer_hapikey` to `crm.extinsions.videoconferencing.settings_api`.
- Added new param `fetch_accounts_uri` to `crm.extinsions.videoconferencing.models.ExternalSettings`.
- Marked `CRM Extensions Accounting Apis` as deprecated.

### CRM clients

- Added `import_template` and `import_source` params to `crm.imports.models.PublicImportResponse`.
- Renamed Api client from `crm.lists.memberships_api()` to `crm.lists.list_app_membership_api()`.
- Renamed Api client from `crm.lists.lists_api()` to `crm.lists.list_app_api()`.
- Changed the type of parameters `list_id` and `list_ids: list[]` from `int` to `string` in all methods of api `crm.lists.list_app_api()`.
- Changed the type of parameters `list_id`, `request_body: list[]` and `source_list_id` from `int` to `string` in all methods of api `crm.lists.list_app_membership_api()`.
- Renamed method `crm.lists.memberships_api.add_remove()` to `crm.lists.list_app_membership_api.add_and_remove()`.
- Renamed `crm.lists.models.CollectionResponseLong` to `crm.lists.models.CollectionResponseJoinTimeAndRecordId`.
- Changed the type of parameter `results: list[int]` to `results: list[JoinTimeAndRecordId]` in `crm.lists.models.CollectionResponseJoinTimeAndRecordId`.
- Changed the type of parameter `list_id`, `business_unit_id`, `subscription_ids: list[]`, `email_id`, `app_id`, `updated_by_id`, `rtype: list[]`, `record_ids_to_remove: list[]`, `record_ids_to_add: list[]`, `record_ids_removed: list[]`, `records_ids_added: list[]` and `record_ids_missing: list[]` from `int` to `string` in all `crm.lists.models` in which these parameters are present.
- Added param `validate_deal_stage_usages_before_delete` to `crm.pipelines.pipelines_api.archive()`, `crm.pipelines.pipelines_api.replace()` and `crm.pipelines.pipelines_api.update()` methods.
- Added `write_permissions` param to `crm.pipelines.models.PipelineStage`.
- Added `description` param to `crm.schemas.models.ObjectTypeDefinitionPatch`.
- Added new params: `option_sort_strategy`, `show_currency_symbol`, `form_field`, `referenced_object_type`, `text_display_hint`, `searchable_in_global_search`
and `number_display_hint` to `crm.schemas.models.ObjectTypePropertyCreate`.

### Marketing client

- Moved methods `archive()`, `create()`, `do_cancel()`, `get_by_id()`, `replace()` and `update()` from `marketing.events.marketing_events_external_api()` to `marketing.events.basic_api`.
- Moved method `do_upsert()` from `marketing.events.marketing_events_external_api()` to `marketing.events.batch_api()`.
- Moved and renamed method `archive_batch()` to `archive()` from `marketing.events.marketing_events_external_api.archive_batch()` to `marketing.events.batch_api.archive()`.
- Moved methods `do_email_upsert_by_id()` and `do_upsert_by_id()` from `marketing.events.marketing_events_external_api()` to `marketing.events.subscriber_state_changes()`.
- Renamed Api `marketing.events.settings_external_api()` to `marketing.events.settings_api()`.
- Added new param `is_large_value` to `marketing.events.models.PropertyValue`.
- Changed the type of parameter `category` from `ErrorCategory` to `string` in `marketing.events.models.StandardError`.
- Added new param `lifecycle_stages` to `marketing.forms.models.HubSpotFormConfiguration`.
- Changed the type of parameter `legal_consent_options` from `object` to `HubSpotFormDefinitionAllOfLegalConsentOptions` in all `marketing.forms.models` where parameter exists.
- Changed the `field_type` parameter, now defaults to `payment_link_radio` instead `file` in `DependentFieldDependentField` in `marketing.forms.models`.
- Renamed `marketing.forms.models.HubSpotFormDefinitionPatchRequestLegalConsentOptions` to `marketing.forms.models.HubSpotFormDefinitionAllOfLegalConsentOptions`.
- Added new parameter `other` to `allowed_values` in `marketing.forms.models`.

### Events, Files and OAuth clients

- Moved client from `files.files` to `files`.
- Added new method `files.files_api.get_metadata()`.
- Added new param `expires_at` to `files.models.File` and `files.models.FileUpdateInput`.
- Changed the type of parameter `category` from `ErrorCategory` to `string` in `files.models.StandardError`.
- Added new query params: `index_table_name`, `index_table_name`,`object_property_propname`, `property_propname` and `id` to `get_page()` method.
- Renamed `events.send_api.behavioral_events_tracking_api()` to `events.send_api.custom_event_data_api()`.
- Added new param `prev` to `events.models.Paging`.
- Removed params `scope_to_scope_group_pks, trial_scopes, trial_scope_to_scope_group_pks` from `oauth.models.AccessTokenInfoResponse`.

### Client APIs

- Added `crm.extensions.calling.recording_settings_api` API.
- Added `crm.companies.gdpr_api` API.
- Added `crm.deals.gdpr_api` API.
- Added `crm.objects.line_items.gdpr_api` API.
- Added `crm.objects.calls.gdpr_api` API.
- Added `crm.objects.communications.gdpr_api` API.
- Added `crm.objects.emails.gdpr_api` API.
- Added `crm.objects.feedback_submissions.gdpr_api` API.
- Added `crm.objects.meetings.gdpr_api` API.
- Added `crm.objects.notes.gdpr_api` API.
- Added `crm.objects.postal_mail.gdpr_api` API.
- Added `crm.objects.tasks.gdpr_api` API.
- Added `crm.objects.products.gdpr_api` API.
- Added `crm.objects.quotes.gdpr_api` API.
- Added `crm.objects.tickets.gdpr_api` API.
- Added `crm.line_items.gdpr_api` API.
- Added `marketing.events.basic_api` API.
- Added `marketing.events.batch_api` API.
- Added `marketing.events.subscriber_state_changes_api` API.

## [8.2.1](https://github.com/HubSpot/hubspot-api-python/compare/v8.2.0...v8.2.1) - 2024-01-25

### Updated

- Added new parameters to the `PublicUser` model in `settings.users.models`:
 - `super_admin`: boolean.
 - `send_welcome_email`: boolean.

## [8.2.0](https://github.com/HubSpot/hubspot-api-python/compare/v8.1.1...v8.2.0) - 2023-12-19

## Added

- `cms.pages` Api client.
- `crm.lists` Api client.
- `crm.objects.goals` Api client.
- `crm.objects.taxes` Api client.
- `events.send` Api client.
- `settings.business_units` Api client.

## [8.1.1](https://github.com/HubSpot/hubspot-api-python/compare/v8.1.0...v8.1.1) - 2023-09-25

## Fix

- fix initializing `developer_hapikey`

## [8.1.0](https://github.com/HubSpot/hubspot-api-python/compare/v8.0.0...v8.1.0) - 2023-08-07

## Removed `hapikey` from

- `automation.actions.callbacks_api` Api.
- `cms` (all Api clients).
- `communication_preferences` (all Api clients).
- `conversations` (all API clients).
- `crm` (all Api clients).
- `events` (all Api clients).
- `files` (all Api clients).
- `marketing.events.settings_external_api` Api.
- `marketing.transactional` Api client.

## Updated

- Change type from `object` to `string` in `cms/hubdb/models/StandardError.category`.
- Change type from `StandardError[]` to `StandardError1[]` in `crm/associations/v4/models/BatchResponseSimplePublicObjectWithErrors.errors`.
- Change type from `ErrorCategory` to `string` in `crm/companies/models/StandardError.category`.
- Change type from `ErrorCategory` to `string` in `crm/contacts/models/StandardError.category`.
- Change type from `ErrorCategory` to `string` in `crm/deals/models/StandardError.category`.
- Change type from `ErrorCategory` to `string` in `crm/lineitems/models/StandardError.category`.
- Change type from `ErrorCategory` to `string` in `crm/objects/calls/models/StandardError.category`.
- Change type from `ErrorCategory` to `string` in `crm/objects/communications/models/StandardError.category`.
- Change type from `ErrorCategory` to `string` in `crm/objects/emails/models/StandardError.category`.
- Change type from `ErrorCategory` to `string` in `crm/objects/feedback_submissions/models/StandardError.category`.
- Change type from `ErrorCategory` to `string` in `crm/objects/meetings/models/StandardError.category`.
- Change type from `ErrorCategory` to `string` in `crm/objects/models/StandardError.category`.
- Change type from `ErrorCategory` to `string` in `crm/objects/notes/models/StandardError.category`.
- Change type from `ErrorCategory` to `string` in `crm/objects/postal_mail/models/StandardError.category`.
- Change type from `ErrorCategory` to `string` in `crm/objects/tasks/models/StandardError.category`.
- Change type from `ErrorCategory` to `string` in `crm/products/models/StandardError.category`.
- Change type from `ErrorCategory` to `string` in `crm/properties/models/StandardError.category`.
- Change type from `ErrorCategory` to `string` in `crm/quotes/models/StandardError.category`.
- Change type from `ErrorCategory` to `string` in `crm/tickets/models/StandardError.category`.
- Change type from `ErrorCategory` to `string` in `webhooks/models/StandardError.category`.
- example in README(SimplePublicObjectInputForCreate)


## [8.0.0](https://github.com/HubSpot/hubspot-api-python/compare/v8.0.0-beta.5...v8.0.0) - 2023-06-12

## Updated

- Fix `utils.get_auth_url()` (don't add empty scopes or optional scopes to OAuth url)

## [8.0.0-beta.6](https://github.com/HubSpot/hubspot-api-python/compare/v8.0.0-beta.5...v8.0.0-beta.6) - 2023-05-17

## Added

- added custom exceptions for Signature
- add associations types

## Updated

- Update README
- remove deprecated `validate_signature`


## [8.0.0-beta.5](https://github.com/HubSpot/hubspot-api-python/compare/v8.0.0-beta.4...v8.0.0-beta.5) - 2023-05-12

## Fix

- add missing `crm.associations.v4.basic_api` Api.

## [8.0.0-beta.4](https://github.com/HubSpot/hubspot-api-python/compare/v8.0.0-beta.3...v8.0.0-beta.4) - 2023-05-12

## Added

- `crm.associations.v4.basic_api` Api.

## Updated

- `crm.associations.types_api` -> `crm.associations.schema.types_api`.
- `crm.associations.v4.definitions_api` -> `crm.associations.v4.schema.definitions_api`.
-

## [8.0.0-beta.3](https://github.com/HubSpot/hubspot-api-python/compare/v8.0.0-beta.2...v8.0.0-beta.3) - 2023-05-04

## Added

- `crm.objects.communications` API client

## Updated

- update generated code(v6.5.0)


## [8.0.0-beta.2](https://github.com/HubSpot/hubspot-api-python/compare/v8.0.0-beta.1...v8.0.0-beta.2) - 2023-04-28

## Updated

- Add new event types to webhooks.


## [8.0.0-beta.1](https://github.com/HubSpot/hubspot-api-python/compare/v7.5.0...v8.0.0-beta.1) - 2023-04-06

## Updated

- Rename `cms.hubdb.rows_batch_api.batch_clone_draft_table_rows` -> `cms.hubdb.rows_batch_api.clone_draft_table_rows`.
- Rename `cms.hubdb.rows_batch_api.batch_create_draft_table_rows` -> `cms.hubdb.rows_batch_api.create_draft_table_rows`.
- Rename `cms.hubdb.rows_batch_api.batch_purge_draft_table_rows` -> `cms.hubdb.rows_batch_api.purge_draft_table_rows`.
- Rename `cms.hubdb.rows_batch_api.batch_ReadDrafttable_rows` -> `cms.hubdb.rows_batch_api.read_draft_table_rows`.
- Rename `cms.hubdb.rows_batch_api.batch_read_table_rows` -> `cms.hubdb.rows_batch_api.read_table_rows`.
- Rename `cms.hubdb.rows_batch_api.batch_replace_draft_table_rows` -> `cms.hubdb.rows_batch_api.replace_draft_table_rows`.
- Rename `cms.hubdb.rows_batch_api.batch_update_draft_table_rows` -> `cms.hubdb.rows_batch_api.update_draft_table_rows`.
- `cms.hubdb.tables_api.get_draft_table_details_by_id` -> `cms.hubdb.tables_api.get_draft_table_details_by_id(+include_foreign_ids: bool)`
- `cms.hubdb.tables_api.get_table_details` -> `cms.hubdb.tables_api.get_table_details(+include_foreign_ids: bool)`
- `cms.hubdb.tables_api.update_draft_table` -> `cms.hubdb.tables_api.update_draft_table(+include_foreign_ids: bool)`
- Removed `crm.companies.associations_api`.
- Removed `crm.contacts.associations_api`.
- Removed `crm.deals.associations_api`.
- Removed `crm.line_items.associations_api`.
- Removed `crm.objects.calls.associations_api`.
- Removed `crm.objects.emails.associations_api`.
- Removed `crm.objects.feedback_submissions.associations_api`.
- Removed `crm.objects.meetings.associations_api`.
- Removed `crm.objects.notes.associations_api`.
- Removed `crm.objects.postal_mail.associations_api`.
- Removed `crm.objects.tasks.associations_api`.
- Removed `crm.products.associations_api`.
- Removed `crm.quotes.associations_api`.
- Removed `crm.tickets.associations_api`.
- `crm.companies.basic_api.create(SimplePublicObjectInput -> SimplePublicObjectInputForCreate)`
- `crm.companies.batch_api.create(BatchInputSimplePublicObjectInput -> BatchInputSimplePublicObjectInputForCreate)`
- `crm.contacts.basic_api.create(SimplePublicObjectInput -> SimplePublicObjectInputForCreate)`
- `crm.contacts.batch_api.create(BatchInputSimplePublicObjectInput -> BatchInputSimplePublicObjectInputForCreate)`
- `crm.deals.basic_api.create(SimplePublicObjectInput -> SimplePublicObjectInputForCreate)`
- `crm.deals.batch_api.create(BatchInputSimplePublicObjectInput -> BatchInputSimplePublicObjectInputForCreate)`
- `crm.line_items.basic_api.create(SimplePublicObjectInput -> SimplePublicObjectInputForCreate)`
- `crm.line_items.batch_api.create(BatchInputSimplePublicObjectInput -> BatchInputSimplePublicObjectInputForCreate)`
- `crm.objects.basic_api.create(SimplePublicObjectInput -> SimplePublicObjectInputForCreate)`
- `crm.objects.batch_api.create(BatchInputSimplePublicObjectInput -> BatchInputSimplePublicObjectInputForCreate)`
- `crm.objects.calls.basic_api.create(SimplePublicObjectInput -> SimplePublicObjectInputForCreate)`
- `crm.objects.calls.batch_api.create(BatchInputSimplePublicObjectInput -> BatchInputSimplePublicObjectInputForCreate)`
- `crm.objects.emails.basic_api.create(SimplePublicObjectInput -> SimplePublicObjectInputForCreate)`
- `crm.objects.emails.batch_api.create(BatchInputSimplePublicObjectInput -> BatchInputSimplePublicObjectInputForCreate)`
- `crm.objects.feedback_submissions.basic_api.create(SimplePublicObjectInput -> SimplePublicObjectInputForCreate)`
- `crm.objects.feedback_submissions.batch_api.create(BatchInputSimplePublicObjectInput -> BatchInputSimplePublicObjectInputForCreate)`
- `crm.objects.meetings.basic_api.create(SimplePublicObjectInput -> SimplePublicObjectInputForCreate)`
- `crm.objects.meetings.batch_api.create(BatchInputSimplePublicObjectInput -> BatchInputSimplePublicObjectInputForCreate)`
- `crm.objects.notes.basic_api.create(SimplePublicObjectInput -> SimplePublicObjectInputForCreate)`
- `crm.objects.notes.batch_api.create(BatchInputSimplePublicObjectInput -> BatchInputSimplePublicObjectInputForCreate)`
- `crm.objects.postal_mail.basic_api.create(SimplePublicObjectInput -> SimplePublicObjectInputForCreate)`
- `crm.objects.postal_mail.batch_api.create(BatchInputSimplePublicObjectInput -> BatchInputSimplePublicObjectInputForCreate)`
- `crm.objects.tasks.basic_api.create(SimplePublicObjectInput -> SimplePublicObjectInputForCreate)`
- `crm.objects.tasks.batch_api.create(BatchInputSimplePublicObjectInput -> BatchInputSimplePublicObjectInputForCreate)`
- `crm.objects.products.basic_api.create(SimplePublicObjectInput -> SimplePublicObjectInputForCreate)`
- `crm.objects.products.batch_api.create(BatchInputSimplePublicObjectInput -> BatchInputSimplePublicObjectInputForCreate)`
- `crm.objects.quotes.basic_api.create(SimplePublicObjectInput -> SimplePublicObjectInputForCreate)`
- `crm.objects.quotes.batch_api.create(BatchInputSimplePublicObjectInput -> BatchInputSimplePublicObjectInputForCreate)`
- `crm.objects.tickets.basic_api.create(SimplePublicObjectInput -> SimplePublicObjectInputForCreate)`
- `crm.objects.tickets.batch_api.create(BatchInputSimplePublicObjectInput -> BatchInputSimplePublicObjectInputForCreate)`
- `marketing.events.marketing_events_external_api.do_search` -> `marketing.events.search_api.do_search`
- Rename `oauth.access_tokens_api.get_accessToken` -> `oauth.access_tokens_api.get`.
- Rename `oauth.refresh_tokens_api.archive_refresh_token` -> `oauth.refresh_tokens_api.archive`.
- Rename `oauth.refresh_tokens_api.get_refreshToken` -> `oauth.refresh_tokens_api.get`.
- Rename `oauth.tokens_api.create_token` -> `oauth.tokens_api.create`.

## Added

- Added param `properties` to `crm.properties.core_api.get_all`.
- Added param `properties` to `crm.properties.core_api.get_by_name`.
- Added `high_value` param to all Filters.

## [7.5.0](https://github.com/HubSpot/hubspot-api-python/compare/v7.4.0...v7.5.) - 2023-03-02

 ### Added

- Update models for `crm.properties` API client


## [7.4.0](https://github.com/HubSpot/hubspot-api-python/compare/v7.3.1...v7.4.) - 2023-02-20

 ### Added

- `crm.associations.v4` API client
- `crm.imports.public_imports_api` API client
- `crm.extensions.cards.sample_response_api` API client
- possibility to set limit param for `fetch_all` func

### Fixed

 - Fix `auth.oauth.refresh_tokens_api.archive_refresh_token` method

## [7.3.1](https://github.com/HubSpot/hubspot-api-python/compare/v7.3.0...v7.3.1) - 2023-02-09

 ### Added

- added search by date example in README.

 ### Fixed

- fixed access to `crm.associations.types_api`

## [7.3.0](https://github.com/HubSpot/hubspot-api-python/compare/v7.2.2...v7.3.0) - 2023-01-04

 ### Added

- Signature's util 'HubSpot.utils.signature'
- test coverage for regen

 ### Deprecated

- webhook's util 'HubSpot.utils.webhooks'

## [7.2.2](https://github.com/HubSpot/hubspot-api-python/compare/v7.2.1...v7.2.2) - 2023-01-03

## Added

- missing object_type and association_type (were removed during regen)

## [7.2.1](https://github.com/HubSpot/hubspot-api-python/compare/v7.2.0...v7.2.1) - 2022-12-23

## Fixed

- Added (pipeline_audits_api, pipeline_stage_audits_api) to crm.pipelines discovery

## [7.2.0](https://github.com/HubSpot/hubspot-api-python/compare/v7.1.0...v7.2.0) - 2022-12-19

### Added

- crm.objects.calls API client

## [7.1.0](https://github.com/HubSpot/hubspot-api-python/compare/v7.0.0...v7.1.0) - 2022-12-07

### Changed

- Added Private App access token to cms.domains and crm.imports

### Fixed

- Fix all association APIs


## [7.0.0](https://github.com/HubSpot/hubspot-api-python/compare/v6.1.0...v7.0.0) - 2022-11-14

### Changed (Breaking changes)

- marketing.events updates

## [6.1.0](https://github.com/HubSpot/hubspot-api-python/compare/v6.0.0...v6.1.0) - 2022-10-17

### Changed

- Reduced memory consumtion

## [6.0.0](https://github.com/HubSpot/hubspot-api-python/compare/v5.1.1...v6.0.0) - 2022-08-12

### Changed

- Dropped unsupported versions of Python

## [5.1.0](https://github.com/HubSpot/hubspot-api-python/compare/v5.0.1...v5.1.0) - 2022-06-27

### Added

- CRM Public Object API clients

### Fixed

- returned id_property support for CRM API clients

## [5.0.1](https://github.com/HubSpot/hubspot-api-python/compare/v5.0.0...v5.0.1) - 2022-05-14

### Changed

- OneOfHubSpotFormDefinition model changed to HubSpotFormDefinition

## [5.0.0](https://github.com/HubSpot/hubspot-api-python/compare/v4.0.6...v5.0.0) - 2022-04-12

### Added

- cms.source_code API client
- crm.objects.calls API client
- crm.objects.emails API client
- crm.objects.meetings API client
- crm.objects.notes API client
- crm.objects.tasks API client
- marketing.forms API client
- marketing.events API client
- settings.users API client

### Changed (no discovery breaking changes)

- cms.blogs.authors.author_api -> cms.blogs.authors.blog_authors_api
- cms.blogs.blog_posts.default_api -> cms.blogs.blog_posts.blog_posts_api
- cms.blogs.tags.default_api -> cms.blogs.tags.blog_tags_api

## [4.0.2](https://github.com/HubSpot/hubspot-api-python/compare/v4.0.1...v4.0.1) - 2021-11-03

### Added

- crm.objects.get_all() method

## [4.0.1](https://github.com/HubSpot/hubspot-api-python/compare/v4.0.0...v4.0.1) - 2021-10-07

### Added

- missing object_type and account_type (were removed during regen)

## [4.0.0](https://github.com/HubSpot/hubspot-api-python/compare/v3.8.2...v4.0.0) - 2021-09-08

### Added

- crm.objects.gdpr_api API client
- crm.contacts.gdpr_api API client

### Changed (breaking changes)

- oauth api client regenerated
- cms.audit_logs.default_api -> cms.audit_logs.audit_logs_api
- cms.blogs.authors.default_api -> cms.blogs.authors.author_api
- cms.blogs.blog_posts.default_api -> cms.blogs.blog_posts.blog_post_api
- cms.blogs.tags.default_api -> cms.blogs.tags.tag_api
- cms.performance.default_api -> cms.performance.public_performance_api
- cms.site_search.default_api -> cms.site_search.public_api
- crm.imports.default_api -> crm.imports.public_imports_api
- crm.owners.default_api -> crm.owners.owners_api
- crm.schemas.default_api -> crm.schemas.public_object_schemas_api and crm.schemas.core_api
- marketing.transactional.default_api -> marketing.transactional.public_smtp_tokens_api and
marketing.transactional.single_send_api

## [3.8.0](https://github.com/HubSpot/hubspot-api-python/compare/v3.7.2...v3.8.0) - 2021-06-09

### Added

- communication preferences API client

## [3.7.0](https://github.com/HubSpot/hubspot-api-python/compare/v3.6.1...v3.7.0) - 2021-02-19

### Added

- events API client
- conversations.visitor_identification API client

## [3.6.0](https://github.com/HubSpot/hubspot-api-python/compare/v3.5.1...v3.6.0) - 2021-02-08

### Added

- crm.extensions.accounting API client
- crm.extensions.calling API client
- crm.extensions.videoconferencing API client
- crm.objects.feedback_submissions API client
- marketing.transactional API client
- files.files API client

## [3.5.1](https://github.com/HubSpot/hubspot-api-python/compare/v3.5.0...v3.5.1) - 2021-01-22

### Fixed

- fix batch methods in `cms.blogs` API clients

## [3.5.0](https://github.com/HubSpot/hubspot-api-python/compare/v3.4.2...v3.5.0) - 2021-01-21

### Added

- HubSpot API key support to `automation.actions` API client

## [3.4.2](https://github.com/HubSpot/hubspot-api-python/compare/v3.4.1...v3.4.2) - 2020-12-07

### Fixed

- Fixed hubspot.crm.extensions module init

## [3.4.1](https://github.com/HubSpot/hubspot-api-python/compare/v3.4.0...v3.4.1) - 2020-12-04

### Fixed

- Fixed Blog Posts API (it was not generated by unknown reason)

## [3.4.0](https://github.com/HubSpot/hubspot-api-python/compare/v3.3.0...v3.4.0) - 2020-12-04

### Added

- HubSpot API key support to `cms.blogs.authors` API client
- HubSpot API key support to `cms.blogs.blog_posts` API client
- HubSpot API key support to `cms.blogs.tags` API client
- Standard Errors

## [3.3.0](https://github.com/HubSpot/hubspot-api-python/compare/v3.2.0...v3.3.0) - 2020-10-23

### Added

- HubSpot API key support to `cms.hubdb` API client
- Long description to [PyPi](https://pypi.org/project/hubspot-api-client/) package

## [3.2.0](https://github.com/HubSpot/hubspot-api-python/compare/v3.1.0...v3.2.0) - 2020-10-19

### Added

- `cms.hubdb` API client

## [3.1.0](https://github.com/HubSpot/hubspot-api-python/compare/v3.0.0...v3.1.0) - 2020-08-05

### Added

- `crm.objects` API client
- `crm.chemas` API client

### Updated

- Minor changes in existing clients

## [3.0.0](https://github.com/HubSpot/hubspot-api-python/compare/v2.1.0...v3.0.0) - 2020-08-05

### Incompatible Changes

- `webhooks.SubscriptionListResponse.enabled` field is renamed to `active`

### Added

- new `HubSpot` - a shortage to `hubspot.Client`

## [2.1.0](https://github.com/HubSpot/hubspot-api-python/compare/v2.0.0...v2.1.0) - 2020-06-23

### Added

- OAuth to `cms.audit_logs` API client

### Fixed

- Parsing response in `cms.site_search.default_api.get_by_id` method

## [2.0.0](https://github.com/HubSpot/hubspot-api-python/compare/v1.2.0...v2.0.0) - 2020-06-16

### Incompatible Changes

- `crm.imports.core_api.get_all` method is replaced with `crm.imports.core_api.get_page`

## [1.2.0](https://github.com/HubSpot/hubspot-api-python/compare/v1.1.0...v1.2.0) - 2020-06-12

### Added

- `cms.audit_logs` API client
- `cms.domains` API client
- `cms.performance` API client
- `cms.site_search` API client
- `cms.url_redirects` API client

## [1.1.0](https://github.com/HubSpot/hubspot-api-python/compare/v1.0.0...v1.1.0) - 2020-05-26

### Added

- `validate_signature` method to webhooks utils

## [1.0.0](https://github.com/HubSpot/hubspot-api-python/compare/v1.0.0-beta...v1.0.0) - 2020-04-30

### Added

- This CHANGELOG.md file.
- Batch API client for webhooks
- [PyTest](https://docs.pytest.org/en/latest/) support

### Fixed

- Typos in README

### Incompatible Changes

- Dropped support for Python 3.4
- Renamed webhooks `delete` method to `archive`

## [1.0.0-beta](https://github.com/HubSpot/hubspot-api-python/releases/tag/v1.0.0-beta) - 2020-04-16
