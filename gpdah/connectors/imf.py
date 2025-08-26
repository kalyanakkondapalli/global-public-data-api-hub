import httpx
from typing import List, Dict, Any
from ..models import DatasetInfo
from ..provenance import provenance

class IMFConnector:
    name = "imf"
    base = "https://dataservices.imf.org/REST/SDMX_JSON.svc"

    def list_datasets(self) -> List[DatasetInfo]:
        # Simplified example with one dataset
        return [
            DatasetInfo(
                id="IFS",
                title="International Financial Statistics",
                description="IMF IFS dataset",
                source="IMF Data",
                license="IMF Open License",
                tags=["economics", "finance"]
            )
        ]

    def get_metadata(self, dataset_id: str) -> Dict[str, Any]:
        return {
            "id": dataset_id,
            "source": "IMF",
            "endpoint": f"{self.base}/DataStructure/{dataset_id}"
        }

    def fetch(self, dataset_id: str, params: Dict[str, Any]) -> List[Dict[str, Any]]:
        # Simplified placeholder; real IMF queries use SDMX format
        url = f"{self.base}/CompactData/{dataset_id}/M.US.PCPI_IX"
        q = {"startPeriod": params.get("start", "2015"), "endPeriod": params.get("end", "2020")}
        with httpx.Client(timeout=30) as client:
            r = client.get(url, params=q)
            r.raise_for_status()
            data = r.json()
        # Simplified result parsing
        return [{
            "dataset": dataset_id,
            "params": q,
            "raw": data,
            "provenance": provenance("IMF", dataset_id)
        }]
