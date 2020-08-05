# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased](https://github.com/HubSpot/hubspot-api-python/compare/v3.0.0...HEAD)

## [3.0.0](https://github.com/HubSpot/hubspot-api-python/compare/v1.1.0...v1.2.0) - 2020-08-05

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
