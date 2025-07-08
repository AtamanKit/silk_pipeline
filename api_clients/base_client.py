import requests
from typing import Optional


class BaseAPIClient:
    BASE_URL: str
    TOKEN: str
    LIMIT: int = 100

    def __init__(self, token: str):
        self.TOKEN = token

    def _make_request(self, url: str, method: str = 'POST', data: Optional[dict] = None) -> Optional[dict]:
        try:
            response = requests.request(
                method,
                url,
                headers={"accept": "application/json", "token": self.TOKEN},
                json=data or {},
                timeout=10,
            )
            response.raise_for_status()
            return response.json()
        except requests.ResquestException as e:
            print(f"API request failed: {e}")
            return None
