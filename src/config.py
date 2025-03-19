import os

from dotenv import load_dotenv

class TlsConfig:
    def __init__(self, ak: str, sk: str, region: str, endpoint: str, token: str = ""):
        self.ak = ak
        self.sk = sk
        self.region = region
        self.endpoint = endpoint
        self.token = token


load_dotenv()

TLS_CONFIG = TlsConfig(
    ak=os.getenv("AK"),
    sk=os.getenv("SK"),
    region=os.getenv("REGION"),
    endpoint=os.getenv("ENDPOINT"),
    token=os.getenv("TOKEN", "")
)