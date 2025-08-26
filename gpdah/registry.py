from typing import Dict
from .connectors import WorldBankConnector, WHOConnector, NOAAConnector
from .connectors.imf import IMFConnector
from .connectors.eurostat import EurostatConnector

def get_registry() -> Dict[str, object]:
    return {
        "worldbank": WorldBankConnector(),
        "who": WHOConnector(),
        "noaa": NOAAConnector(),
        "imf": IMFConnector(),
        "eurostat": EurostatConnector(),
    }
