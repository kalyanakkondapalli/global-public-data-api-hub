import httpx
from typing import List, Dict, Any
from ..models import DatasetInfo
from ..provenance import provenance

class EurostatConnector:
    name = "eurostat"
    base = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data"

    def list_datasets(self) -> List[DatasetInfo]:
        return [
            DatasetInfo(
                id="demo_pjan",
                title="Population on 1 January by age and sex",
                description="Eurostat demographic dataset",
                source="Eurostat",
                license="Eurostat reuse policy",
                tags=["population", "demographics"]
            )
        ]

    def get_metadata(self, dataset_id: str) -> Dict[str, Any]:
        return {
            "id": dataset_id,
            "source": "Eurostat",
            "endpoint": f"{self.base}/{dataset_id}"
        }

    def fetch(self, dataset_id: str, params: Dict[str, Any]) -> List[Dict[str, Any]]:
        url = f"{self.base}/{dataset_id}"
        with httpx.Client(timeout=30) as client:
            r = client.get(url, params={"size": params.get("limit", 10)})
            r.raise_for_status()
            data = r.json()
        # Simplified parsing: just return first N observations
        obs = data.get("value", {})
        records = []
        for idx, val in list(obs.items())[: params.get("limit", 10)]:
            records.append({
                "obs_index": idx,
                "value": val,
                "provenance": provenance("Eurostat", dataset_id)
            })
        return records
