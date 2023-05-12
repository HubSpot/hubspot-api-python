# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased](https://github.com/HubSpot/hubspot-api-python/compare/v8.0.0-beta.5...HEAD)

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

- new `HubSpot` class - a shortage to `hubspot.Client`

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
