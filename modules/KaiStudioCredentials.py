class KaiStudioCredentials:
    organization_id: str
    instance_id: str
    api_key: str
    host: str

    def __init__(self,organization_id: str, api_key: str, instance_id: str, host: str):
        self.organization_id = organization_id
        self.instance_id = instance_id
        self.api_key = api_key
        self.host = host
