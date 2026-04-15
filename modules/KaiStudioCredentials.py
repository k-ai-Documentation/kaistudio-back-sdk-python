from typing import Optional


class KaiStudioCredentials:
    host: Optional[str]
    token: Optional[str]

    def __init__(self, token: Optional[str] = None, host: Optional[str] = None):
        self.token = token
        self.host = host
