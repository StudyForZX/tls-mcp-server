from config import TLS_CONFIG
from volcengine.tls.TLSService import TLSService

class TlsResource:
    """
        火山引擎tls日志资源类
    """

    client: TLSService = None

    def __init__(self):
        self.client = TLSService(
            endpoint=TLS_CONFIG.endpoint,
            region=TLS_CONFIG.region,
            access_key_id=TLS_CONFIG.ak,
            access_key_secret=TLS_CONFIG.sk,
            security_token=TLS_CONFIG.token
        )