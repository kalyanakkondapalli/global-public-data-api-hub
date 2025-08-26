# 🌍 Global Public Data API Hub (GPD-AH)

[![PyPI version](https://img.shields.io/pypi/v/gpdah?color=blue)](https://pypi.org/project/gpdah/)
[![Docker Pulls](https://img.shields.io/docker/pulls/YOUR-DOCKER-USER/gpdah)](https://hub.docker.com/r/YOUR-DOCKER-USER/gpdah)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A **FastAPI-based, unified hub** for accessing **global public datasets** (World Bank, WHO, IMF, Eurostat, NOAA). Provides standardized REST API, ETL pipelines, and reproducible data access for **researchers, journalists, policy-makers, and developers**.

## ✨ Features
- ✅ Unified API for heterogeneous datasets (World Bank, IMF, Eurostat, WHO, NOAA)
- ✅ Swagger/OpenAPI documentation with examples
- ✅ JOSS-ready paper and citation support
- ✅ Reproducible ETL pipelines with caching and provenance
- ✅ Docker & GitHub Pages-ready docs

## 📦 Installation

```bash
git clone https://github.com/YOUR-USERNAME/global-public-data-api-hub.git
cd global-public-data-api-hub
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -U pip
pip install -e .[dev]
```

## 🚀 Run Locally

```bash
uvicorn gpdah.api:app --reload
# Swagger UI: http://127.0.0.1:8000/docs
# ReDoc: http://127.0.0.1:8000/redoc
```

## 🧪 Tests

```bash
pytest -q
pytest --cov=gpdah
ruff check .
```

## 🐳 Docker

```bash
docker build -t gpdah .
docker run -p 8000:8000 gpdah
# or docker-compose up --build
```

## 📊 Example Queries

```bash
curl http://127.0.0.1:8000/v1/datasets
curl "http://127.0.0.1:8000/v1/query?dataset_id=worldbank:NY.GDP.MKTP.CD&date=2015:2021&limit=5"
curl "http://127.0.0.1:8000/v1/query?dataset_id=eurostat:demo_pjan&limit=5"
curl "http://127.0.0.1:8000/v1/query?dataset_id=imf:IFS&limit=2"
```

## 📓 Jupyter Demo

```bash
jupyter notebook notebooks/demo.ipynb
```

## 🌐 SEO / Discoverability

- Keywords: open data, public datasets, fastapi, api, data pipeline, climate data, health data, economics, reproducible research
- GitHub topics: open-data, public-datasets, fastapi, api, data-pipeline, climate-data, health-data, economics, research-tool
- Swagger UI and ReDoc embedded with rich descriptions for search engines

## 📖 Citation & JOSS

The repository contains a JOSS-ready paper (`paper/paper.md`) and bibliography (`paper/paper.bib`).
Follow JOSS submission instructions: https://joss.theoj.org/