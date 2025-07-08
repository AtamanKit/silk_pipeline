from typing import Generator
from .base_client import BaseAPIClient


class CrowdstrikeClient(BaseAPIClient):
    BASE_URL = "https://api.recruiting.app.silk.security/api/crowdstrike/hosts/get"

    def fetch_hosts(self) -> Generator[dict, None, None]:
        skip = 0
        while True:
            url = f"{self.BASE_URL}?skip={skip}&limit={self.LIMIT}"
            data = self._make_request(url)
            if not data or not data.get("hosts"):
                break
            for host in data["hosts"]:
                yield host
            skip += self.LIMIT
