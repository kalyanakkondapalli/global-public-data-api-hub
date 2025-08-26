---
title: 'Global Public Data API Hub: A Unified Interface for Open Datasets'
authors:
  - name: Kalyana Krishna Kondapalli
    orcid: 0009-0003-0832-259X
    affiliation: 1
affiliations:
  - name: Independent Researcher
    index: 1
date: 2025-08-26
bibliography: paper.bib
---

# Summary

The Global Public Data API Hub (GPD-AH) is an open-source Python/FastAPI framework that
standardizes access to public datasets (climate, health, economics, demographics) via
pluggable connectors. It provides discoverability, schema-normalized responses, provenance
metadata, and reproducible ETL pipelines suitable for research, policy analysis, and journalism.

# Statement of need

Public datasets are dispersed across heterogeneous APIs with inconsistent formats,
pagination, authentication, and metadata conventions. This fragmentation increases the
engineering burden on researchers and analysts and impedes reproducible workflows. GPD-AH
addresses these issues by offering a small, extensible framework that (1) unifies access to
multiple providers via a connector interface, (2) provides machine-readable metadata and
provenance, and (3) offers reproducible ETL primitives and caching to reduce redundant work.

# State of the field

Several client libraries and SDKs exist for specific providers (for example, the World Bank,
Eurostat, and IMF SDKs). However, there is a lack of lightweight, provider-agnostic tooling
that exposes a consistent HTTP API and is easy to deploy for reproducible research. GPD-AH
fills that gap by focusing on discoverability, provenance, and extensibility.

# Software description

- **Language:** Python (>=3.9)
- **License:** MIT
- **Core dependencies:** FastAPI, HTTPX, Pydantic
- **Design:** Pluggable connector interface (`BaseConnector`), a registry, ETL pipelines, and an HTTP API.
- **Provenance:** Each record includes provenance metadata (source, dataset id, retrieval timestamp, and software version).
- **Deployment:** Local (`uvicorn`), Docker, or containerized via `docker-compose`.
- **Testing & CI:** `pytest`, `ruff` for linting, and GitHub Actions for CI.

# Example

Start a local server and query World Bank GDP values:

```bash
uvicorn gpdah.api:app --reload
# GET /v1/datasets
# GET /v1/query?dataset_id=worldbank:NY.GDP.MKTP.CD&date=2015:2021&limit=50
```

# Availability, support, and reuse potential

The project is released under an MIT license and is designed for easy reuse: new connectors
can be implemented by subclassing `BaseConnector` and registering them. The API is
documented via OpenAPI/Swagger. GPD-AH is useful for analysts, journalists, and policy
researchers who need consistent programmatic access to public data.

# Acknowledgements

The author thanks maintainers of FastAPI and data providers who publish open APIs.

# References
