import httpx


class KnowledgeBaseModule:
    def __init__(self, base_url: str, headers: dict):
        self.__base_url = base_url.rstrip('/') + '/studio/knowledge-base'
        self.__headers = headers

    async def list_available_kb_type(self) -> list:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/list-available-kb-type", headers=self.__headers)
            return response.json()['response'] if response.status_code == 200 else response.text

    async def get_credentials_for_by_type(self, kb_type: str) -> dict:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/get-credentials-for-by-type", headers=self.__headers,
                                         json={"kb_type": kb_type})
            return response.json()['response'] if response.status_code == 200 else response.text

    async def get_kb_type_from_internal_type(self, kb_type: str) -> str:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            response = await client.post(f"{self.__base_url}/get-kb-type-from-internal-type", headers=self.__headers,
                                         json={"kb_type": kb_type})
            return response.json()['response'] if response.status_code == 200 else response.text
